# How to add new labels to i18n file #

Note: This is not a complete "how to". Only covers adding new labels to an existing po file.

## Precondition: ##
> Environment must be configured as [SetupDevelopmentEnvironment](SetupDevelopmentEnvironment.md) explains.

## Steps: ##

1.- Add a new label to a template:
```
	{{ _('About vikuit') }}
```
2.- Look for every po file you want to translate:
```
	conf/locale/es/LC_MESSAGES/django.po
```
3.- Search for your label in file to ensure is not available already. Application shows an error when a label is duplicated.

4.- Add these lines replacing quoted content by your current label and translation.
```
	msgid "About vikuit"
	msgstr "Acerca de vikuit"
```
5.- Compile messages to generate a mo file. (Django uses mo file to recover a translation. A label added to po file but not compiled in mo file can not be found).
```
	<PATH_TO_YOUR_GAE_SDK>/lib/django_0_96/django/bin/compile-messages.py
```
![http://www.vikuit.com/file/googlecodevikuit/img/compileMSG.png](http://www.vikuit.com/file/googlecodevikuit/img/compileMSG.png)

6.- Finally run command.