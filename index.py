#tree
from Tree import options
from crud import crud,adv,custom
from console import *
#index
options.addData({ 
    "main": {
        "function":main,
        "content": {
            "help": {"function": help},
            "quit": {"function":quit_program},
            "create": {"function":crud.create},
            "read": {"function":crud.read},
            "update": {"function":crud.update},
            "delete": {"function":crud.delete},
            "search": {"function":adv.search},
            "custom": {
                "function":adv.custom,
                "content": {
                    "read": {"function":custom.read},
                    "manipulate": {"function":custom.manipulate}
                }
            }
        }
    }
})