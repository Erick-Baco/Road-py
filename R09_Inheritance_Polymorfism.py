# EJERCICIO:
# Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# implemente una superclase Animal y un par de subclases Perro y Gato,
# junto con una función que sirva para imprimir el sonido que emite cada Animal.

class Animal:
    def __init__(self, specie: str, weight: float) -> None:
        self.specie: str = specie
        self.weight: float = weight

    def sonido(self) -> None:
        pass


class Perro(Animal):

    def __init__(self, weight: float) -> None:
        super().__init__("Dog", weight)

    def sonido(self) -> None:
        print(f"Ladrar {self.weight}")


class Gato(Animal):

    def __init__(self, weight: float) -> None:
        super().__init__("Cat", weight)

    def sonido(self) -> None:
        print(f"Mauyar {self.weight}")


bob: Perro = Perro(3.2)
bob.sonido()

rob: Gato = Gato(5.5)
rob.sonido()


# DIFICULTAD EXTRA (opcional):
# Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre.
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# actividad, y almacenan los empleados a su cargo.


class Employee:

    def __init__(self, id: str, name: str, last_name: str, cargo: str) -> None:
        self.id: str = id
        self.name: str = name
        self.last_name: str = last_name
        self.cargo: str = cargo

    def work(self):
        print(f"{self.name} is working")


class Programmer(Employee):

    def __init__(self, id: str, name: str, last_name: str, pm) -> None:
        super().__init__(id, name, last_name, "Programador")
        self.boss = pm.name

    def work(self) -> None:
        print(f"{self.name} is working as {self.cargo} for {self.boss}")


class ProjectManager(Employee):

    def __init__(self, id: str, name: str, last_name: str, manager, team: list[Programmer]) -> None:
        super().__init__(id, name, last_name,"Gerente de proyectos")
        self.team: list[Programmer] = team
        self.boss: str = manager.name

    def work(self) -> None:
        print(f"{self.name} ({self.id}) is working as {self.cargo} for {self.boss}")

    def prTeam(self) -> None:
        print(f"{self.name}´s team:")
        for i in self.team:
            print(f"\t{i.name}")


class Manager(Employee):

    def __init__(self, id: str, name: str, last_name: str, team: list[ProjectManager]) -> None:
        super().__init__(id,name,last_name,"Gerente")
        self.team: list[ProjectManager] = team

    def work(self) -> None:
        print(f"{self.name} is working as {self.cargo}")

    def pmTeam(self) -> None:
        print(f"{self.name}´s team:")
        for i in self.team:
            print(f"\t{i.name}")


boss: Manager = Manager("001","Bob","Alviter",[])
boss.work()

pm1: ProjectManager = ProjectManager("101","Erick","Alviter",boss,[])
pm1.work()
pm2: ProjectManager = ProjectManager("102","Morgan","Perro",boss,[])
pm2.work()

boss.team.append(pm1)
boss.team.append(pm2)
boss.pmTeam()

pr1: Programmer = Programmer("201","Eder","Xxx",pm1)
pr1.work()
pr2: Programmer = Programmer("202","Lili","Yyy",pm1)
pr2.work()
pr3: Programmer = Programmer("203","Perez","Yyy",pm2)
pr3.work()
pr4: Programmer = Programmer("203","Juan","Yyy",pm2)
pr4.work()

pm1.team.append(pr1)
pm1.team.append(pr2)
pm2.team.append(pr3)
pm2.team.append(pr4)

pm1.prTeam()
pm2.prTeam()
