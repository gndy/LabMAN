from django.contrib import admin
from django import forms
from .models import UserFile
from django.contrib.contenttypes.admin import GenericStackedInline
import util


class UserFileForm(forms.ModelForm):
    class Meta:
        model=UserFile

        exclude = ("size", "mime_type", )

    def clean(self,*args, **kwargs):
        """Custom validation method to update mime-type and size fields."""
        data=super(UserFileForm,self).clean(*args, **kwargs)
        try:
            data["mime_type"]=UserFile.get_mime(data["content"])
            data["size"]=data["content"].size
        except AttributeError:
            raise forms.ValidationError("Could not determine file's mime type")

    def clean_description(self):
        return util.clean_html(self.cleaned_data['description'])

class FileInlineAdmin(GenericStackedInline):
    """An inline editor form for Images."""
    model = UserFile
    exclude=["mime_type","size"]
    can_delte=False
    verbose_name="File"
    verbose_name_plural="Files"
    extra=0
    fieldsets=(
        (None,{"fields":(("category","tag","owner"),"description","content",)}),
    )
    suit_classes = 'suit-tab suit-tab-files'


# Register your models here.
@admin.register(UserFile)
class UserFile_Admin(admin.ModelAdmin):
    form = UserFileForm
    exclude = ("mime_type","size",)
    list_display = ("category","tag","mime_type","safe_description",)

    related_lookup_fields = {
        'fk': ['owner'],
        'generic': [['content_type', 'object_id'], ],
    }
    fieldsets=(
        (None,{"fields":(("category","tag"),"description","content")}),
        ("Linking",{"fields":("owner",("content_type","object_id"),),'classes': ('grp-collapse grp-closed',)}),

    )
