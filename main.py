class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.name}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        self.save_tasks()

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def view_tasks(self):
        print("\nTamamlanmamış Görevler:")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}. {task}")

        print("\nTamamlanmış Görevler:")
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    self.tasks.append(Task(name, completed == "True"))
        except FileNotFoundError:
            pass


def main():
    manager = TaskManager()

    while True:
        print("\nYapılacaklar Listesi:")
        print("1. Görev Ekle")
        print("2. Görev Tamamla")
        print("3. Görev Sil")
        print("4. Görevleri Görüntüle")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            task_name = input("Eklenecek görev adı: ")
            manager.add_task(task_name)
        elif choice == "2":
            manager.view_tasks()
            task_index = int(input("Tamamlanacak görev numarası: "))
            manager.mark_task_completed(task_index)
        elif choice == "3":
            manager.view_tasks()
            task_index = int(input("Silinecek görev numarası: "))
            manager.delete_task(task_index)
        elif choice == "4":
            manager.view_tasks()
        elif choice == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
