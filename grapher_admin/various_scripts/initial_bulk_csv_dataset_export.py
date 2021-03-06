import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import grapher_admin.wsgi
from grapher_admin.views import write_dataset_csv
from grapher_admin.models import Dataset, Variable
from django.conf import settings

# use this script to make the initial csv and metadata export of all datasets to the repo

all_datasets = Dataset.objects.all()

for each in all_datasets:
    last_updated_by = Variable.objects.filter(datasetId=each).order_by('-updated_at')
    if last_updated_by:
        committer = last_updated_by.first()
        if not committer.uploaded_by:
            committer_name = settings.DATASETS_REPO_USERNAME
            committer_email = settings.DATASETS_REPO_EMAIL
        else:
            committer_name = committer.uploaded_by.get_full_name()
            committer_email = committer.uploaded_by.email
        write_dataset_csv(each.pk, each.name, None, committer_name, committer_email)
