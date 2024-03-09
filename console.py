#!/usr/bin/python3
'''
This is the console module
'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' This is the class definition for the console. '''
    prompt = '(hbnb) '

    def do_create(self, arg):
        '''Creates new instance of the BaseModel class.
        '''
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        cls_name = arg_list[0]
        print(cls_name)

        if cls_name not in self.classes():
            print(self.classes())
            print("** class doesn't exist **")
            return

        new_ = eval(f"{cls_name}()")
        new_.save()
        print(new_.id)
        return

    def do_show(self, arg):
        ''' Prints the string representation of an instance
        '''
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        cls_name = arg_list[0]

        if cls_name not in self.classes():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        key = f"{cls_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
        '''
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        cls_name = arg_list[0]

        if cls_name not in self.classes():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        key = f"{cls_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances
        '''
        obj = []
        if not arg:
            for ob in storage.all().values():
                obj.append(str(ob))
            print(obj)
            return

        arg_list = arg.split()
        cls_name = arg_list[0]

        if cls_name not in self.classes():
            print("** class doesn't exist **")
            return

        for key, value in storage.all().itens():
            if cls_name == key.split('.')[0]:
                obj.append(str(value))

        print(obj)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id
        '''
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        cls_name = arg_list[0]

        if cls_name not in self.classes():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        key = f"{cls_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attr_name = arg_list[2]
        attr_val = arg_list[3]

        attr_type = type(getattr(storage.all()[key], attr_name))
        if attr_type == int:
            attr_val = int(attr_val)
        elif attr_type == float:
            attr_val = float(attr_val)

        setattr(storage.all()[key], attr_name, attr_val)
        storage.all()[key].save()

    def classes(self):
        ''' returns list of classes
        '''
        return ([key.split('.')[0] for key in storage.all().keys()])

    def do_emptyLine(self):
        ''' Do nothing empty line is entered
        '''
        pass

    def do_EOF(self, line):
        ''' This is the end-of-file command which quits the program
        '''
        return (True)

    def do_quit(self, line):
        ''' This is a command to quit the program
        '''
        exit()

    def default(self, line):
        '''The default command for unknown commands'''
        print(f"Unknown command: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
