import psutil
from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def _get_curr_val(self):
        ...

    @abstractmethod
    def _result_update(self, a):
        ...

    @abstractmethod
    def get_data(self):
        self._result_update(self._get_curr_val())


class CpuInfo(Abstract):
    result_cpu = {}

    def _get_curr_val(self):
        freq_cpu = psutil.cpu_freq()
        count_cpu = psutil.cpu_count()
        even_cpu = {
            'cpu' + str(key): val for key in range(1, psutil.cpu_count(logical=True) + 1)
            for val in psutil.cpu_percent(interval=1, percpu=True)
        }
        times_cpu = psutil.cpu_times()

        return freq_cpu, count_cpu, even_cpu, times_cpu

    def _result_update(self, getval):
        self.result_cpu.update(current_freq=getval[0].current)
        self.result_cpu.update(count_cpu=getval[1])
        self.result_cpu.update(getval[2])
        self.result_cpu.update(user_time=getval[3].user,
                               system_time=getval[3].system,
                               idle_time=getval[3].idle)

    def get_data(self):
        Abstract.get_data(self)

    def __str__(self):
        return 'Информация о процессоре: \n' + \
               ('текущая частота процессора: {current_freq} Гц \n'
                'количество используемых процессоров: {count_cpu} \n'
                'проценты использования процессоров: {cpu1}%, {cpu2}%, {cpu3}% \n'
                'время, затрачиваемое процессами в пользовательском режиме: {user_time} с \n'
                'время, затрачиваемое процессами в режиме ядра: {system_time} с \n'
                'время простоя: {idle_time} с')\
                .format(**self.result_cpu)


class MemoryInfo(Abstract):
    memory_result = {}

    def _get_curr_val(self):
        memory_data = psutil.virtual_memory()
        return memory_data

    def _result_update(self, getval):
        self.memory_result.update(total_memory=getval.total,
                                  available=getval.available,
                                  percent=getval.percent,
                                  free=getval.free)

    def get_data(self):
        Abstract.get_data(self)

    def __str__(self):
        return 'Информация о памяти: \n' + \
               ('общая память: {total_memory} б \n'
                'доступная память: {available} б \n'
                'процент использования памяти:{percent}% \n'
                'свободная память: {free} б')\
                .format(**MemoryInfo.memory_result)


class ProcessInfo(Abstract):
    process_result = {}

    def _get_curr_val(self):
        process_data = psutil.Process()
        return process_data

    def _result_update(self, getval):
        self.process_result.update(name=getval.name(),
                                   exe=getval.exe(),
                                   status=getval.status(),
                                   create_time=getval.create_time())

    def get_data(self):
        Abstract.get_data(self)

    def __str__(self):
        return 'Информация о процессах: \n' + \
               ('имя процесса: {name} \n'
                'путь к исполняемому файлу: {exe} \n'
                'статус процесса: {status} \n'
                'время создания процесса: {create_time} мс')\
                .format(**ProcessInfo.process_result)


class DiskInfo(Abstract):
    disk_result = {}

    def _get_curr_val(self):
        disk_data = psutil.disk_usage('/')
        return disk_data

    def _result_update(self, getval):
        self.disk_result.update(total=float(getval.total),
                                used=getval.used,
                                free=getval.free,
                                percent=getval.percent)

    def get_data(self):
        Abstract.get_data(self)

    def __str__(self):
        return 'Информация о батарее: \n' + \
               ('информация об общей памяти диска: {total} б \n'
                'информация об использованной памяти диска: {used} б \n'
                'информация о свободной памяти диска: {free} б \n'
                'использованная память в процентах: {percent}%')\
                .format(**DiskInfo.disk_result)


def main():
    cpu = CpuInfo()
    cpu.get_data()
    print(cpu, '\n')
    memory = MemoryInfo()
    memory.get_data()
    print(memory, '\n')
    process = ProcessInfo()
    process.get_data()
    print(process, '\n')
    disk = DiskInfo()
    disk.get_data()
    print(disk)


if __name__ == '__main__':
    main()
