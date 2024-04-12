#!/usr/bin/python3
"""The Entry Point of the command interpreter"""
import cmd
from models.__init__ import classes
from models.__init__ import storage
from models.__init__ import types


class HBNBCommand(cmd.Cmd):
    """this is the Entry point of command interpreter
    it has functions `quit` `EOF` `help`
    with custom prompt `(hbnb)`"""
    Intro = ''
    prompt = '(hbnb)'

    def do_create(self, args):
        """Creates a new instance of `BaseModel`,
        saves it `(to the JSON file)`and prints the `id`"""
        if not args:
            self.stdout.write("** class name missing **\n")
        elif args not in classes.keys():
            self.stdout.write("** class doesn't exist **\n")
        else:
            instance = classes[args]()
            instance.save()
            self.stdout.write(f"{instance.id}\n")

    def do_show(self, args):
        """Prints the string representation of an instance\n
        based on the class name and id.

        Ex: $ show BaseModel 1234-"""
        cmds, arg, string = self.parseline(args)
        line = string.split(' ')
        class_obj, class_id = line[0], line[1:]
        if not class_obj:
            self.stdout.write("** class name missing **\n")
            return
        if class_obj not in classes.keys():
            self.stdout.write("** class doesn't exist **\n")
            return
        if not class_id or len(class_id) > 1:
            self.stdout.write("** instance id missing **\n")
            return

        key = str(class_obj) + '.' + str(class_id[0])
        storage_copy = storage.all()
        try:
            self.stdout.write(f"{storage_copy[key]}\n")
            return
        except KeyError:
            self.stdout.write("** no instance found **\n")
            return

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        cmds, arg, string = self.parseline(args)
        line = string.split(' ')
        class_obj, class_id = line[0], line[1:]
        if not class_obj:
            self.stdout.write("** class name missing **\n")
            return
        if class_obj not in classes.keys():
            self.stdout.write("** class doesn't exist **\n")
            return
        if not class_id or len(class_id) > 1:
            self.stdout.write("** instance id missing **\n")
            return
        stored_items_ids = \
            [keys.split('.')[1] for keys in storage.all().keys()]
        if class_id[0] not in stored_items_ids:
            self.stdout.write("** no instance found **\n")
            return
        key = str(class_obj) + '.' + str(class_id[0])
        # storage_copy = storage.all()
        # print(len(storage_copy))
        storage.delete(key)
        # self.stdout.write(f"Deleted {key}\n")
        # print(len(storage_copy))
        return
        # except TypeError:
        #     self.stdout.write("** no instance found **\n")
        #     return

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name"""
        data = storage.all()
        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in classes:
                self.stdout.write("** class doesn't exist **\n")
                return
            result = [str(v) for k, v in data.items()
                      if k.split('.')[0] == args]
        else:
            result = [str(v) for k, v in data.items()]
        self.stdout.write(f"{result}\n")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage: update <class name> <id>
        <attribute name> "<attribute value>"
        """
        line = args.split(' ')
        # print(line)
        # declaration
        list_of_args = {}
        list_of_args_keys = ["cls_obj", "cls_id", "attr_name", "attr_val"]
        i = 0
        try:
            while i < len(line):
                if len(line[0]) < 1:
                    self.stdout.write("** class name missing **\n")
                    return
                if i > 3:
                    # print(line[3])
                    concat_attr_value = line[3:]
                    list_of_args[list_of_args_keys[3]] = \
                        ' '.join(concat_attr_value)
                    # print(list_of_args[list_of_args_keys[3]])
                    # print(line[3])
                    break
                list_of_args[list_of_args_keys[i]] = line[i]
                i += 1
        except IndexError:
            pass
        # class name check
        if "cls_obj" not in list_of_args.keys():
            self.stdout.write("** class name missing **\n")
            return
        if list_of_args["cls_obj"] not in classes.keys():
            self.stdout.write("** class doesn't exist **\n")
            return
        # ids check
        ids = [k.split('.')[1] for k in storage.all().keys()]
        if "cls_id" not in list_of_args.keys():
            self.stdout.write("** instance id missing **\n")
            return
        if list_of_args["cls_id"] not in ids:
            self.stdout.write("** no instance found **\n")
            return
        # attribute name check
        if "attr_name" not in list_of_args.keys():
            self.stdout.write("** attribute name missing **\n")
            return
        # not allowed attribute names
        if list_of_args["attr_name"] in ['id', 'created_at', 'updated_at']:
            return
        # attribute value check
        if "attr_val" not in list_of_args.keys():
            self.stdout.write("** value missing **\n")
            return
        print(type(list_of_args["attr_val"]))
        if list_of_args["attr_name"] in types.keys():
            list_of_args["attr_val"] = types[list_of_args["attr_name"]](
                list_of_args["attr_val"].replace(
                    '\"', '')
            )

        # Start Updates
        print(type(list_of_args["attr_val"]))
        try:
            kwargs = {list_of_args["attr_name"]: list_of_args["attr_val"].replace(
                '\"', '')}
        except AttributeError:
            kwargs = {list_of_args["attr_name"]: list_of_args["attr_val"]}
        # print(kwargs)
        key = list_of_args["cls_obj"] + '.' + list_of_args["cls_id"]
        # print(key)
        storage.update(key, kwargs)

    def do_EOF(self, args):
        """EOF command"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.
        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
