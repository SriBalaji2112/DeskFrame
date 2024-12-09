from customtkinter import CTkFont


def get_font(font, font_size, font_style, font_weight):
    font_style = font_style.lower() if font_style is not None else None
    font_weight = font_weight.lower() if font_weight is not None else None
    # 01
    if font is not None and font_size is not None and font_style is not None \
            and font_weight is not None:
        font = CTkFont(family=font, size=font_size,
                       weight=font_weight if font_weight == "bold" else 'normal',
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 02
    elif font is not None and font_size is not None and font_style is None \
            and font_weight is None:
        font = CTkFont(family=font, size=font_size)
    # 03
    elif font is not None and font_size is None and font_style is not None \
            and font_weight is None:
        font = CTkFont(family=font,
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 04
    elif font is not None and font_size is None and font_style is None \
            and font_weight is not None:
        font = CTkFont(family=font, size=font_size,
                       weight=font_weight if font_weight == "bold" else 'normal')
    # 05
    elif font is not None and font_size is not None and font_style is not None \
            and font_weight is None:
        font = CTkFont(family=font, size=font_size,
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 06
    elif font is not None and font_size is not None and font_style is None \
            and font_weight is not None:
        font = CTkFont(family=font, size=font_size,
                       weight=font_weight if font_weight == "bold" else 'normal',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 07
    elif font is not None and font_size is None and font_style is not None \
            and font_weight is not None:
        font = CTkFont(family=font,
                       weight=font_weight if font_weight == "bold" else 'normal',
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 08
    elif font is None and font_size is not None and font_style is not None \
            and font_weight is None:
        font = CTkFont(size=font_size,
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 09
    elif font is None and font_size is not None and font_style is None \
            and font_weight is not None:
        font = CTkFont(size=font_size,
                       weight=font_weight if font_weight == "bold" else 'normal',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 10
    elif font is None and font_size is not None and font_style is not None \
            and font_weight is not None:
        font = CTkFont(size=font_size,
                       weight=font_weight if font_weight == "bold" else 'normal',
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    # 11
    elif font is None and font_size is None and font_style is not None \
            and font_weight is not None:
        font = CTkFont(weight=font_weight if font_weight == "bold" else 'normal',
                       slant=font_style if font_style == "italic" else 'roman',
                       underline=font_style if font_style == "underline" else False,
                       overstrike=font_style if font_style == "overstrike" else False
                       )
    else:
        font = CTkFont(family="arial", size=13)
    return font
