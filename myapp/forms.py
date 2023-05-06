from django import forms
# The widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.


class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', min_length=1, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

# attrs = {'class':'form-control'} adding bootstrap class form-control into forms
# to make form responsive
    subject = forms.CharField(label='Subject Description', min_length=1,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))

    email = forms.CharField(label='Email', min_length=1, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    
    # roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    # will give an text besides the roll_num

    # 404 error handling page  -- will be rendered on an invalid route/ url pattern 
