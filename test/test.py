from databaker.constants import *

def per_file(tabs):
    return "*"


def collapse_bag(bag):
    # get top_left cell and remove from collection

    # TODO TEST TEST TEST TEST TEST
    def collapse_one():
        (left, top) = min(cells)  # TODO reverse? not mandatory
        (right, bottom) = (left, top)
        cells.remove((left, top))

        while True:
            if (right+1, bottom) in cells:
                right += 1
                cells.remove((right, bottom))
            else:
                break

        while True:
            for col in range(left, right+1):
                if (col, bottom+1) not in cells:
                    return ((left, top), (right, bottom))
            bottom += 1
            for col in range(left, right+1):
                cells.remove((col, bottom))

    cells = set((cell.x, cell.y) for cell in bag)
    while cells:
        yield collapse_one()



def per_tab(tab):
    tab.dimension("kitten", "kitten")
    tab.excel_ref("A1").fill(RIGHT).dimension('top', DIRECTLY, ABOVE)
    foo = tab.excel_ref("A1").fill(RIGHT).fill(DOWN)
    print list(collapse_bag(foo))
    x = tab.filter("x")
    print list(collapse_bag(x))
    print tab.excel_ref("A6").value
    print tab.excel_ref("A6").parent()
    print tab.get_at(0,5)

    print tab.one_of(["anchorspan", "a3"]).parent()
    print tab.excel_ref("A6:B7")
    print tab.excel_ref("A:B")
    print tab.excel_ref("2:3")
    return tab.excel_ref("B2").fill(RIGHT).fill(DOWN)

