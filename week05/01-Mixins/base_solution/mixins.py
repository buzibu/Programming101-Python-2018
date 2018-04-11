import json


class Jsonable:
    serializable_types = (
        int,
        float,
        str,
        list,
        bool,
        dict,
        type(None),
    )

    def prepare_for_serialization(self):
        class_name = self.__class__.__name__
        dict_ = {}

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                dict_[k] = v
            elif isinstance(v, Jsonable):
                dict_[k] = v.prepare_for_serialization()
            else:
                raise ValueError(f'{v} is not Serializable!')

        return {'class_name': class_name, 'dict': dict_}

    def to_json(self):
        return json.dumps(self.prepare_for_serialization(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        # TODO
        pass
