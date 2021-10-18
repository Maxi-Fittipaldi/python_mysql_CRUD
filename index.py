#tree
from Tree import options
from crud import crud,adv,custom
from console import console
#index
options.addData({ 
    "main": {
        "function":console.main,
        "content": {
            "help": {"function": console.help},
            "quit": {"function":console.quit_program},
            "create": {"function":crud.create},
            "read": {"function":crud.read},
            "update": {"function":crud.update},
            "delete": {"function":crud.delete},
            "search": {"function":adv.search},
            "custom": {
                "function":adv.custom,
                "content": {
                    "go_back": {"function": custom.go_back},
                    "read": {"function":custom.read},
                    "manipulate": {"function":custom.manipulate}
                }
            }
        }
    }
})