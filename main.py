from pandas import DataFrame
from pandas.io.formats.style import Styler
from dataframe_image import export
import os


CARD_DATA = [
    ["6", "", "28", "", "47", "", "63", "", "89"],
    ["", "", "20", "34", "", "53", "", "70", "86"],
    ["", "11", "", "32", "45", "51", "", "77", ""]
]
BARREL_DATA = [
    [False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, True, False, False, False],
    [False, False, False, True, False, False, False, True, False]
]
BARREL_IMG_PATH = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "barrel.png"
).replace("\\", "/")

RED = '#E20D13'
SHIFT_I = 1
SHIFT_J = 2
PLAYER = 'Stanislav'
CARD_NUM = 18


def main():
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    df = DataFrame(CARD_DATA, columns=columns, index=["1", "2", "3"])

    table_styles = get_table_styles()
    df_styled = df.style.set_table_styles(table_styles)
    df_styled.pipe(set_caption)

    export(df_styled, "df_styled.png")


def get_table_styles() -> list[dict]:
    t_styles = [
        {
            'selector': 'th', 'props': 'text-align: center; background-color: white;'
        },
        {
            'selector': 'th:nth-child(1)', 'props': 'border-top: 1px solid white;'
        },
        {
            'selector': 'td', 'props': [
                ('font-size', '24pt'), ('font-weight', 'bold'), ('border', '1px solid black'),
                ('text-align', 'center'), ('width', '44px'), ('border-color', 'black')
            ]
        },
        {
            'selector': 'caption', 'props': [
                ('text-align', 'left'), ('font-size', '12pt'), ('font-weight', 'normal'), ('font-style', 'italic')
            ]
        }
    ]

    # SET BARRELS
    for i, row in enumerate(CARD_DATA):
        for j, cell in enumerate(row):
            props = [
                ('background-repeat', 'no-repeat'), ('background-position', 'center'), ('background-size', '64px 64px'),
                ('background-image', f'url("{BARREL_IMG_PATH}")'), ('color', RED)
            ] if (CARD_DATA[i][j].isdigit() and BARREL_DATA[i][j] is True) else []

            t_styles.append({'selector': f'tr:nth-child({i + SHIFT_I}) td:nth-child({j + SHIFT_J})', 'props': props})

    return t_styles


def set_caption(styler: Styler):
    styler.set_caption(f'Карта №{CARD_NUM}<br>Игрок - {PLAYER}')


if __name__ == "__main__":
    main()
