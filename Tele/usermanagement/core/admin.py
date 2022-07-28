from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import User
from django  import forms
from .models import Area, Bouquet, Device, Plans, Ticket, User,Channel,Subscription,Ticket,Invoice
from daterange.filters import DateRangeFilter
# Register your models here.

# admin.site.register(Area)
# admin.site.register(Device)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ['email', 'first_name', 'last_name', 'password1', 'password2']
                        + ['pincode','phone_number','alternate_number','gst','zone','department','mpos_serial_number','mpos_user_name','area', 'assigned_devices']
            }
        ),
    )
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header

            {
                'fields': (
                    'pincode','phone_number','alternate_number','gst','zone','department','mpos_serial_number','mpos_user_name','area', 'assigned_devices',
                ),
            },
        ),
    )





class AreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')
    search_fields = ['code', 'description']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'iemi_number','service_provider')
    search_fields = ['name', 'iemi_number','service_provider']

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','number')
    search_fields = ['name', 'price','number']


class BouqetAdmin(admin.ModelAdmin):
    list_display = ('name','get_channels','price')
    def get_channels(self, obj):
        return "\n".join([p.name for p in obj.channels.all()])
    search_fields = ['name','channels__name','price']

class PlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_bouq','get_channels','price','types')
    def get_channels(self, obj):
        return "\n".join([p.name for p in obj.channels.all()])
    def get_bouq(self, obj):
        return "\n".join([p.name for p in obj.bouqets.all()])
    search_fields = ['name', 'bouqets__name','channels__name','price','types']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'plan', 'user', 'created_at')
    search_fields = ['name', 'plan__name', 'user__first_name', 'created_at']
    list_filter = ['plan__name']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('supscription', 'pgid', 'invoice_created_at', 'status')
    search_fields = ['supscription__name', 'pgid', 'invoice_created_at', 'status']
    list_filter = [('status'), ('invoice_created_at', DateRangeFilter)]

class TicketAdmin(admin.ModelAdmin):
    list_display = ('from_customer', 'assigned_to', 'type_ticket', 'message','status')
    search_fields = ['from_customer__first_name', 'assigned_to__first_name', 'type_ticket', 'message','status']
    list_filter = ['assigned_to__first_name', 'type_ticket','status' ]


admin.site.register(Area,AreaAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(User,CustomUserAdmin)
admin.site.register(Channel,ChannelAdmin)
admin.site.register(Bouquet,BouqetAdmin)
admin.site.register(Plans,PlansAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Ticket,TicketAdmin)