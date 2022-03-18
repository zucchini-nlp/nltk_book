
def pprint_iob(tree):
    final = ""
    for num in range(len(tree)):
        try:
            tree[num].label()
        except AttributeError:
            final += ("\n" + tree[num][0] + " " + tree[num][1] + " O")
        else:
            for idx, leaf in enumerate(list(tree[num].leaves())):
                if len(tree[num].leaves()) == 1:
                    final += ("\n" + leaf[0] + " " + leaf[1] + " B-" + tree[num].label())
                elif idx == 0:
                    final += ("\n" + tree[num].leaves()[0][0] + " " + tree[num].leaves()[0][1] + " B-" + tree[num].label())
                else:
                    final += ("\n" + tree[num].leaves()[idx][0] + " " + tree[num].leaves()[idx][1] + " I-" + tree[num].label())
           
    print(final)
    


def pprint_tree(tree):
    final = "(S"
    for num in range(len(tree)):
        try:
            tree[num].label()
        except AttributeError:
            final += ("\n  " + tree[num][0] + "/" + tree[num][1])
        else:
            final += ("\n  (" + tree[num].label())
            for leaf in tree[num].leaves():
                final += (" " + leaf[0] + "/" + leaf[1])
            final += ")"
    final += ")"            
    print(final)