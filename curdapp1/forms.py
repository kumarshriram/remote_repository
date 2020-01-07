from django import  forms
class InsertingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter your product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Product_id',
                'class':'form-control'
            }
        )
    )
    product_name=forms.CharField(
        label='Enter Your Product',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Product_name',
                'class': 'form-control'

            }
        )
    )
    product_cost=forms.CharField(
        label='Enter Your Product Cost',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Product_cost',
                'class': 'form-control'
            }
        )
    )
    product_class=forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Product_class',
                'class': 'form-control'
            }
        )
    )
    no_of_products=forms.IntegerField(
        label='Enter Your No. Of Products',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your  no_of_Product',
                'class': 'form-control'
            }
        )
    )
    y=range(2022,1960)
    manufacture_date=forms.DateTimeField(
        label='Enter your Manufacture Date',
        widget=forms.SelectDateWidget(years=y,
            attrs={
                'placeholder': 'Your Product  manufacture_date',
                'class': 'form-control'
            }
        )
    )
    expiry_date=forms.DateTimeField(
        label='Enter Your Expiry Date',
        widget=forms.SelectDateWidget(
            attrs={
                'placeholder': 'Your Product expiry_date',
                'class': 'form-control'
            }
        )
    )
    customer_name=forms.CharField(
        label='Enter Your customer name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your customer_name',
                'class': 'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Your Mobile',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your_mobile',
                'class': 'form-control'
            }
        )
    )
    email=forms.EmailField(
        label='Enter your email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your_email',
                'class': 'form-control'
            }
        )
    )
class UpdateDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter your product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Product_id',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.CharField(
        label='Enter Your Product Cost',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Product_cost',
                'class': 'form-control'
            }
        )
    )
class DeleteDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enteer your product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Product_id',
                'class': 'form-control'
            }
        )
    )