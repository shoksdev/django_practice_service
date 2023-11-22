from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    # name = forms.CharField(label='Название', widget=forms.TextInput, required=True)
    # descript = forms.CharField(label='Описание', widget=forms.Textarea, required=True)
    # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), required=True)
    # photo = forms.ImageField(
    #     label='Фото помещения или план', widget=forms.FileInput,
    #     help_text='Изображения должно быть в одном из форматов (jpg, jpeg, png, bmp) и с максимальным размером 2 МБ',
    #     required=True)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        image_types = ['.jpg', '.jpeg', '.png', '.bpm']
        for image_type in image_types:
            if image_type in str(image) and image.size <= 2097152:
                return image

        raise forms.ValidationError(
            "Ошибка: "
            "Файл должен иметь формат: jpg, jpeg, png, bmp и размер не более 2МБ"
        )

    class Meta:
        model = Application
        fields = ('title', 'description', 'category', 'image', )
