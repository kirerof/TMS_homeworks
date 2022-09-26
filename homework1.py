import psutil


class CpuInfo:
    result_cpu = {}
    cpu_template = ('текущая частота процессора: {current_freq} Гц \n'
                    'количество используемых процессоров: {count_cpu} \n'
                    'проценты использования процессоров: {cpu1}%, {cpu2}% \n'
                    'время, затрачиваемое процессами в пользовательском режиме: {user_time} с \n'
                    'время, затрачиваемое процессами в режиме ядра: {system_time} с \n'
                    'время простоя: {idle_time} с')

    def get_data(self):
        freq_cpu = psutil.cpu_freq()
        CpuInfo.result_cpu.update(current_freq=freq_cpu.current)

        count_cpu = psutil.cpu_count()
        CpuInfo.result_cpu.update(count_cpu=count_cpu)

        percent_cpu = psutil.cpu_percent(interval=1, percpu=True)
        even_cpu = {
            'cpu' + str(key): val for key in range(1, psutil.cpu_count(logical=True) + 1)
            for val in percent_cpu
        }
        CpuInfo.result_cpu.update(even_cpu)

        times_cpu = psutil.cpu_times()
        CpuInfo.result_cpu.update(user_time=times_cpu.user,
                                  system_time=times_cpu.system,
                                  idle_time=times_cpu.idle)

        return CpuInfo.result_cpu

    def __str__(self):
        return 'Информация о процессоре: \n' +\
               CpuInfo.cpu_template.format(**CpuInfo.result_cpu)


class MemoryInfo:
    memory_result = {}
    memory_template = ('общая память: {total_memory} б \n'
                       'доступная память: {available} б \n'
                       'процент использования памяти:{percent}% \n'
                       'свободная память: {free} б')

    def get_data(self):
        memory_data = psutil.virtual_memory()
        MemoryInfo.memory_result.update(total_memory=memory_data.total,
                                        available=memory_data.available,
                                        percent=memory_data.percent,
                                        free=memory_data.free)

        return MemoryInfo.memory_result

    def __str__(self):
        return 'Информация о памяти: \n' + \
               MemoryInfo.memory_template.format(**MemoryInfo.memory_result)


class ProcessInfo:
    process_result = {}
    process_template = ('имя процесса: {name} \n'
                        'путь к исполняемому файлу: {exe} \n'
                        'статус процесса: {status} \n'
                        'время создания процесса: {create_time} мс')

    def get_data(self):
        process_data = psutil.Process()
        ProcessInfo.process_result.update(name=process_data.name(),
                                          exe=process_data.exe(),
                                          status=process_data.status(),
                                          create_time=process_data.create_time())

        return ProcessInfo.process_result

    def __str__(self):
        return 'Информация о процессах: \n' + \
               ProcessInfo.process_template.format(**ProcessInfo.process_result)


class DiskInfo:
    disk_result = {}
    disk_template = ('информация об общей памяти диска: {total} б \n'
                     'информация об использованной памяти диска: {used} б \n'
                     'информация о свободной памяти диска: {free} б \n'
                     'использованная память в процентах: {percent}%')

    def get_data(self):
        disk_data = psutil.disk_usage('/')
        DiskInfo.disk_result.update(total=float(disk_data.total),
                                    used=disk_data.used,
                                    free=disk_data.free,
                                    percent=disk_data.percent)

        return DiskInfo.disk_result

    def __str__(self):
        return 'Информация о батарее: \n' + \
               DiskInfo.disk_template.format(**DiskInfo.disk_result)


def main():
    cpu = CpuInfo()
    cpu.get_data()
    print(cpu)
    print()
    memory = MemoryInfo()
    memory.get_data()
    print(memory)
    print()
    process = ProcessInfo()
    process.get_data()
    print(process)
    print()
    disk = DiskInfo()
    disk.get_data()
    print(disk)


if __name__ == '__main__':
    main()
