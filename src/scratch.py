from data_model import Query, Category, Data

if __name__ == "__main__":
    q = Query(text="SELECT 1")
    q2 = Query(text="SELECT 2")

    c1 = Category(name="CAT 1")
    c2 = Category(name="CAT 2")

    q.categories = [c1, c2]
    q2.categories = [c1]

    d = Data()
    d.add_query(q)
    d.add_query(q2)

    for cat in d.categories:
        if cat == c1:
            assert cat.queries == {q, q2}
        else:
            assert cat.queries == {q}

    assert len(d.queries) == 2
