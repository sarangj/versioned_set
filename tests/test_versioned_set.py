import versioned_set


def test_version():
    assert versioned_set.__version__ == '0.1.0'


def test_versioned_set():
    s = versioned_set.VersionedSet()
    s.add(1)
    s.add(2)
    s.remove(4)
    s.remove(1)
    assert sorted(s.members(1)) == [1]
    assert sorted(s.members(2)) == [1, 2]
    assert sorted(s.members(3)) == [2]


def test_versioned_set_long():
    s = versioned_set.VersionedSet()
    for i in range(5000):
        s.add(i)

    check_set = set()
    for i in range(20):
        assert set(s.members(i)) == check_set
        check_set.add(i)
