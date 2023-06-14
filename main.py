from pandas import DataFrame
from dataframe_image import export
from PIL import Image
import os


def main():
    card_data = [
        ["6", "", "28", "", "47", "", "63", "", "89"],
        ["", "", "20", "34", "", "53", "", "70", "86"],
        ["", "11", "", "32", "45", "51", "", "77", ""]
    ]
    columns = ["№1", "", "", "", "", "", "", "", ""]
    df = DataFrame(card_data, columns=columns, index=["", "", ""])
    pic_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "circle.png"
    ).replace("\\", "/")
    df_styled = df.style.set_table_styles([
        {
            'selector': 'td',
            'props': [
                ('font-size', '24pt'), ('font-weight', 'bold'), ('border-style', 'solid'), ('border-width', '1px'),
                ('text-align', 'center'), ('background-image', f'url("{pic_path}")'), ('width', '44px'),
                ('background-repeat', 'no-repeat'), ('background-position', 'center'), ('background-size', '64px 64px'),
                ('color', '#8B0000'), ('border-color', 'black')
            ]
        }
    ])
    export(df_styled, "df_styled.png")
    img = Image.open("df_styled.png")
    w, h = img.size
    img.crop((17, 0, w, h)).save("df_styled.png")


if __name__ == "__main__":
    main()
