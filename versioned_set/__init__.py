__version__ = '0.1.0'
import dataclasses
import enum
import typing


class Op(enum.Enum):
    ADD = 1
    REMOVE = 2


@dataclasses.dataclass
class Diff:

    obj: typing.Any
    op: Op


class VersionedSet:

    def __init__(self):
        self.diffs: list[Diff] = []
        self.current = {}

    def add(self, obj):
        if obj not in self.current:
            self.diffs.append(Diff(obj, Op.ADD))
            self.current[obj] = 1

        return len(self.diffs)

    def remove(self, obj):
        try:
            del self.current[obj]
        except KeyError:
            pass
        else:
            self.diffs.append(Diff(obj, Op.REMOVE))

        return len(self.diffs)

    def members(self, version):
        num_versions = len(self.diffs)
        if version > num_versions:
            raise IndexError()

        if version <= num_versions / 2:
            return self._build_members_from_front(version)

        return self._build_members_from_back(version)

    def _build_members_from_front(self, version):
        values = {}
        for i in range(version):
            diff = self.diffs[i]
            if diff.op == Op.ADD:
                values[diff.obj] = 1
            elif diff.op == Op.REMOVE:
                del values[diff.obj]
            else:
                raise ValueError()

        return list(values.keys())

    def _build_members_from_back(self, version):
        values = self.current.copy()
        for i in range(len(self.diffs)-1, version-1, -1):
            print(i)
            diff = self.diffs[i]
            print(diff)
            if diff.op == Op.ADD:
                del values[diff.obj]
            elif diff.op == Op.REMOVE:
                values[diff.obj] = 1
            else:
                raise ValueError()

        return list(values.keys())
