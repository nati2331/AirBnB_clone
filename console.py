#!/usr/bin/python3
"""
Entry point to the AirBnB Console project
"""
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Line-oriented command processor (a command-line interface)
    extending the cmd module.
    """
    prompt = '(hbtn) '

    def __init__(self):
        """
        Initializes class objects.
        """
        cmd.Cmd.__init__(self)
        self.classes = {
            'BaseModel': self.create_BaseModel,
            'User': self.create_User,
            'State': self.create_State,
            'City': self.create_City,
            'Place': self.create_Place,
            'Amenity': self.create_Amenity,
            'Review': self.create_Review
        }

    def do_quit(self, line):
        """Exits the program: <quit> call method implementation."""
        sys.exit(1)

    def help_quit(self):
        """Help for quit command."""
        print('syntax: quit\n--terminates the application')

    def do_EOF(self, line):
        """Exits the program: <Ctrl + D> call method implementation."""
        print()
        return True

    def help_EOF(self):
        """Help for EOF command."""
        print('syntax: Ctrl + D\n--terminates the application')

    def emptyline(self):
        """Override cmd.emptyline - do nothing."""
        pass

    def create_BaseModel(self, **kwargs):
        """Creates a new BaseModel instance."""
        if kwargs:
            return BaseModel(**kwargs)
        else:
            return BaseModel()

    def create_User(self, **kwargs):
        """Creates a new User instance."""
        if kwargs:
            return User(**kwargs)
        else:
            return User()

    def create_State(self, **kwargs):
        """Creates a new State instance."""
        if kwargs:
            return State(**kwargs)
        else:
            return State()

    def create_City(self, **kwargs):
        """Creates a new City instance."""
        if kwargs:
            return City(**kwargs)
        else:
            return City()

    def create_Place(self, **kwargs):
        """Creates a new Place instance."""
        if kwargs:
            return Place(**kwargs)
        else:
            return Place()

    def create_Amenity(self, **kwargs):
        """Creates a new Amenity instance."""
        if kwargs:
            return Amenity(**kwargs)
        else:
            return Amenity()

    def create_Review(self, **kwargs):
        """Creates a new Review instance."""
        if kwargs:
            return Review(**kwargs)
        else:
            return Review()

    def do_create(self, line):
        """<create class_name> creates a new instance of BaseModel,
        saves it (to JSON file), and prints the id (instance's)."""
        if line:
            for class_, method in self.classes.items():
                if class_ in line:
                    new = method()
                    new.save()
                    print(new.id)
                    break
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, line):
        """<show object_id> prints the string representation of
        an instance based on class name and id."""
        if line:
            args = line.split()
            if args[0] and args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objects = storage.all()
                    this_key = f'{args[0]}.{args[1]}'
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            print(str_rep)
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """<destroy class_name object_id> deletes an instance based on
        the class name and id (and saves the change into the JSON file)."""
        if line:
            args = line.split()
            if args[0] and args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objects = storage.all()
                    this_key = f'{args[0]}.{args[1]}'
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            del objects[obj]
                            storage.save()
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """<all> or <all class_name> prints all string representations
        of all instances based or not on the class name."""
        objects = storage.all()
        obj_list = []
        if line:
            for cls in self.classes.keys():
                if line == cls:
                    for obj, val in objects.items():
                        cls_name = (obj.split('.'))[0]
                        if cls_name == line:
                            obj_list.append(str(val))
                    print(obj_list)
                    break
            else:
                print("** class doesn't exist **")
        else:
            for obj, val in objects.items():
                obj_list.append(str(val))
            print(obj_list)

    def do_update(self, line):
        """<update class_name object_id attribute_name attribute_value>
        updates the instance [class_name.object_id]'s attribute
        [attribute_name] to [attribute_value] if [attribute_name]
        already exists. Adds the attribute [name]->[value] pair otherwise
        (and saves the change into the JSON file)."""
        if line:
            args = line.split()
            if args[0] and args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    objects = storage.all()
                    this_key = f'{args[0]}.{args[1]}'
                    for obj, str_rep in objects.items():
                        if obj == this_key:
                            if len(args) > 2:
                                for k, val in (str_rep.to_dict()).items():
                                    if k == args[2]:
                                        if len(args) > 3:
                                            attr_val = type(val)(args[3])
                                            setattr(str_rep, args[2], attr_val)
                                            str_rep.save()
                                        else:
                                            print("** value missing **")
                                        break
                                else:
                                    if len(args) > 3:
                                        setattr(str_rep, args[2], args[3])
                                        str_rep.save()
                                    else:
                                        print("** value missing **")
                            else:
                                print("** attribute name missing **")
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

