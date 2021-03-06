# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-11 14:54
from __future__ import unicode_literals

from django.db import migrations

def standardize_long_unwpp_country_names(apps, schema_editor):
    try:
        Entity = apps.get_model('grapher_admin', 'Entity')

        Entity.objects.filter(name='Serbia,  Including Kosovo.').update(name='Serbia (including Kosovo)')
        Entity.objects.filter(name='Guadeloupe,  Including Saint-Barthélemy and Saint-Martin (French part).').update(name='Guadeloupe (including Saint-Barthélemy and Saint-Martin)')

        DataValue = apps.get_model('grapher_admin', 'DataValue')

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(name='More developed regions, More developed regions comprise Europe, Northern America, Australia/New Zealand and Japan.').pk).update(fk_ent_id=Entity.objects.get(name='More developed regions').pk)
        Entity.objects.get(name='More developed regions, More developed regions comprise Europe, Northern America, Australia/New Zealand and Japan.').delete()


        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Less developed regions, Less developed regions comprise all regions of Africa, Asia (except Japan), Latin America and the Caribbean plus Melanesia, Micronesia and Polynesia.').pk).update(
            fk_ent_id=Entity.objects.get(name='Less developed regions').pk)
        Entity.objects.get(
            name='Less developed regions, Less developed regions comprise all regions of Africa, Asia (except Japan), Latin America and the Caribbean plus Melanesia, Micronesia and Polynesia.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Least developed countries, The group of least developed countries, as defined by the United Nations General Assembly in its resolutions (59/209, 59/210, 60/33, 62/97, 64/L.55, 67/L.43, 64/295 and 68/18) included 47 countries in June  2017:  33 in Africa,').pk).update(
            fk_ent_id=Entity.objects.get(name='Least developed countries').pk)
        Entity.objects.get(
            name='Least developed countries, The group of least developed countries, as defined by the United Nations General Assembly in its resolutions (59/209, 59/210, 60/33, 62/97, 64/L.55, 67/L.43, 64/295 and 68/18) included 47 countries in June  2017:  33 in Africa,').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Less developed regions, excluding least developed countries, Other less developed countries comprise the less developed regions excluding the least developed countries.').pk).update(
            fk_ent_id=Entity.objects.get(name='Less developed regions, excluding least developed countries').pk)
        Entity.objects.get(
            name='Less developed regions, excluding least developed countries, Other less developed countries comprise the less developed regions excluding the least developed countries.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='High-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').pk).update(
            fk_ent_id=Entity.objects.get(name='High-income countries').pk)
        Entity.objects.get(
            name='High-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').pk).update(
            fk_ent_id=Entity.objects.get(name='Middle-income countries').pk)
        Entity.objects.get(
            name='Middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Upper-middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').pk).update(
            fk_ent_id=Entity.objects.get(name='Upper-middle-income countries').pk)
        Entity.objects.get(
            name='Upper-middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Lower-middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').pk).update(
            fk_ent_id=Entity.objects.get(name='Lower-middle-income countries').pk)
        Entity.objects.get(
            name='Lower-middle-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Low-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').pk).update(
            fk_ent_id=Entity.objects.get(name='Low-income countries').pk)
        Entity.objects.get(
            name='Low-income countries, The country classification by income level is based on 2016 GNI per capita from the World Bank.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Sub-Saharan Africa, Sub-Saharan Africa refers to all of Africa except Northern Africa.').pk).update(
            fk_ent_id=Entity.objects.get(name='Sub-Saharan Africa').pk)
        Entity.objects.get(
            name='Sub-Saharan Africa, Sub-Saharan Africa refers to all of Africa except Northern Africa.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Mauritius, Including Agalega, Rodrigues and Saint Brandon.').pk).update(
            fk_ent_id=Entity.objects.get(name='Mauritius').pk)
        Entity.objects.get(
            name='Mauritius, Including Agalega, Rodrigues and Saint Brandon.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='United Republic of Tanzania, Including Zanzibar.').pk).update(
            fk_ent_id=Entity.objects.get(name='Tanzania').pk)
        Entity.objects.get(
            name='United Republic of Tanzania, Including Zanzibar.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Western Africa, Including Saint Helena, Ascension, and Tristan da Cunha.').pk).update(
            fk_ent_id=Entity.objects.get(name='Western Africa').pk)
        Entity.objects.get(
            name='Western Africa, Including Saint Helena, Ascension, and Tristan da Cunha.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='China, For statistical purposes, the data for China do not include Hong Kong and Macao, Special Administrative Regions (SAR) of China, and Taiwan Province of China.').pk).update(
            fk_ent_id=Entity.objects.get(name='China').pk)
        Entity.objects.get(
            name='China, For statistical purposes, the data for China do not include Hong Kong and Macao, Special Administrative Regions (SAR) of China, and Taiwan Province of China.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='China, Hong Kong SAR, As of 1 July 1997, Hong Kong became a Special Administrative Region (SAR) of China.').pk).update(
            fk_ent_id=Entity.objects.get(name='Hong Kong').pk)
        Entity.objects.get(
            name='China, Hong Kong SAR, As of 1 July 1997, Hong Kong became a Special Administrative Region (SAR) of China.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='China, Macao SAR, As of 20 December 1999, Macao became a Special Administrative Region (SAR) of China.').pk).update(
            fk_ent_id=Entity.objects.get(name='Macao').pk)
        Entity.objects.get(
            name='China, Macao SAR, As of 20 December 1999, Macao became a Special Administrative Region (SAR) of China.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='China, Taiwan Province of China').pk).update(
            fk_ent_id=Entity.objects.get(name='Taiwan').pk)
        Entity.objects.get(
            name='China, Taiwan Province of China').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='South-Central Asia, The regions Southern Asia and Central Asia are combined into South-Central Asia.').pk).update(
            fk_ent_id=Entity.objects.get(name='South-Central Asia').pk)
        Entity.objects.get(
            name='South-Central Asia, The regions Southern Asia and Central Asia are combined into South-Central Asia.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Malaysia, Including Sabah and Sarawak.').pk).update(
            fk_ent_id=Entity.objects.get(name='Malaysia').pk)
        Entity.objects.get(
            name='Malaysia, Including Sabah and Sarawak.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Azerbaijan, Including Nagorno-Karabakh.').pk).update(
            fk_ent_id=Entity.objects.get(name='Azerbaijan').pk)
        Entity.objects.get(
            name='Azerbaijan, Including Nagorno-Karabakh.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Cyprus,  Refers to the whole country.').pk).update(
            fk_ent_id=Entity.objects.get(name='Cyprus').pk)
        Entity.objects.get(
            name='Cyprus,  Refers to the whole country.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Georgia,  Including Abkhazia and South Ossetia.').pk).update(
            fk_ent_id=Entity.objects.get(name='Georgia').pk)
        Entity.objects.get(
            name='Georgia,  Including Abkhazia and South Ossetia.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='State of Palestine,  Including East Jerusalem.').pk).update(
            fk_ent_id=Entity.objects.get(name='Palestine').pk)
        Entity.objects.get(
            name='State of Palestine,  Including East Jerusalem.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Czechia').pk).update(
            fk_ent_id=Entity.objects.get(name='Czech Republic').pk)
        Entity.objects.get(
            name='Czechia').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Republic of Moldova,  Including Transnistria.').pk).update(
            fk_ent_id=Entity.objects.get(name='Moldova').pk)
        Entity.objects.get(
            name='Republic of Moldova,  Including Transnistria.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Ukraine,  Including Crimea.').pk).update(
            fk_ent_id=Entity.objects.get(name='Ukraine').pk)
        Entity.objects.get(
            name='Ukraine,  Including Crimea.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Northern Europe,  Including Faeroe Islands, and Isle of Man.').pk).update(
            fk_ent_id=Entity.objects.get(name='Northern Europe').pk)
        Entity.objects.get(
            name='Northern Europe,  Including Faeroe Islands, and Isle of Man.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Channel Islands,  Refers to Guernsey, and Jersey.').pk).update(
            fk_ent_id=Entity.objects.get(name='Channel Islands').pk)
        Entity.objects.get(
            name='Channel Islands,  Refers to Guernsey, and Jersey.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Finland,  Including Åland Islands.').pk).update(
            fk_ent_id=Entity.objects.get(name='Finland').pk)
        Entity.objects.get(
            name='Finland,  Including Åland Islands.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Norway,  Including Svalbard and Jan Mayen Islands.').pk).update(
            fk_ent_id=Entity.objects.get(name='Norway').pk)
        Entity.objects.get(
            name='Norway,  Including Svalbard and Jan Mayen Islands.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Southern Europe,  Including Andorra, Gibraltar, Holy See, and San Marino.').pk).update(
            fk_ent_id=Entity.objects.get(name='Southern Europe').pk)
        Entity.objects.get(
            name='Southern Europe,  Including Andorra, Gibraltar, Holy See, and San Marino.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Spain,  Including Canary Islands, Ceuta and Melilla.').pk).update(
            fk_ent_id=Entity.objects.get(name='Spain').pk)
        Entity.objects.get(
            name='Spain,  Including Canary Islands, Ceuta and Melilla.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='TFYR Macedonia,  The former Yugoslav Republic of Macedonia.').pk).update(
            fk_ent_id=Entity.objects.get(name='Macedonia').pk)
        Entity.objects.get(
            name='TFYR Macedonia,  The former Yugoslav Republic of Macedonia.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Western Europe,  Including Liechtenstein, and Monaco.').pk).update(
            fk_ent_id=Entity.objects.get(name='Western Europe').pk)
        Entity.objects.get(
            name='Western Europe,  Including Liechtenstein, and Monaco.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Caribbean,  Including Anguilla, British Virgin Islands, Caribbean Netherlands, Cayman Islands, Dominica, Montserrat, Saint Kitts and Nevis, Sint Maarten (Dutch part) and Turks and Caicos Islands.').pk).update(
            fk_ent_id=Entity.objects.get(name='Caribbean').pk)
        Entity.objects.get(
            name='Caribbean,  Including Anguilla, British Virgin Islands, Caribbean Netherlands, Cayman Islands, Dominica, Montserrat, Saint Kitts and Nevis, Sint Maarten (Dutch part) and Turks and Caicos Islands.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='South America,  Including Falkland Islands (Malvinas).').pk).update(
            fk_ent_id=Entity.objects.get(name='South America').pk)
        Entity.objects.get(
            name='South America,  Including Falkland Islands (Malvinas).').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='NORTHERN AMERICA,  Including Bermuda, Greenland, and Saint Pierre and Miquelon.').pk).update(
            fk_ent_id=Entity.objects.get(name='Northern America').pk)
        Entity.objects.get(
            name='NORTHERN AMERICA,  Including Bermuda, Greenland, and Saint Pierre and Miquelon.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Australia,  Including Christmas Island, Cocos (Keeling) Islands and Norfolk Island.').pk).update(
            fk_ent_id=Entity.objects.get(name='Australia').pk)
        Entity.objects.get(
            name='Australia,  Including Christmas Island, Cocos (Keeling) Islands and Norfolk Island.').delete()

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Polynesia,  Including American Samoa, Cook Islands, Niue, Pitcairn, Tokelau, Tuvalu, and Wallis and Futuna Islands.').pk).update(
            fk_ent_id=Entity.objects.get(name='Polynesia').pk)
        Entity.objects.get(
            name='Polynesia,  Including American Samoa, Cook Islands, Niue, Pitcairn, Tokelau, Tuvalu, and Wallis and Futuna Islands.').delete()

        Variable = apps.get_model('grapher_admin', 'Variable')
        Dataset = apps.get_model('grapher_admin', 'Dataset')
        DataValue.objects.filter(fk_var_id__in=Variable.objects.filter(fk_dst_id__in=Dataset.objects.filter(namespace='faostat')), fk_ent_id=Entity.objects.get(code='FSM').pk).update(fk_ent_id=Entity.objects.get(name='Micronesia,  Including Marshall Islands, Nauru, Northern Mariana Islands, and Palau.').pk)

        DataValue.objects.filter(fk_ent_id=Entity.objects.get(
            name='Micronesia (Federated States of)').pk).update(
            fk_ent_id=Entity.objects.get(code='FSM').pk)
        Entity.objects.get(name='Micronesia (Federated States of)').delete()
        Entity.objects.filter(code='FSM').update(name='Micronesia (country)')
        Entity.objects.filter(name='Micronesia,  Including Marshall Islands, Nauru, Northern Mariana Islands, and Palau.').update(name='Micronesia (region)')
    except Exception:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('grapher_admin', '0009_fix_map_colorSchemeValuesAutomatic'),
    ]

    operations = [
        migrations.RunPython(standardize_long_unwpp_country_names),
    ]
