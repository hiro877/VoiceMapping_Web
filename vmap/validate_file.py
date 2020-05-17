def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.wav', '.mp3', '.acc']  # 受け取り可能な拡張子をここに記述
    print(ext)
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'対応していない拡張子です。')