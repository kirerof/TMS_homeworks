import psutil


def cpu_info():
    cpu_result = {}
    cpu_data = psutil.cpu_freq()
    cpu_result.update(current_freq=cpu_data.current)
    return cpu_result


def memory_info():
    memory_result = {}
    memory_data = psutil.virtual_memory()
    memory_result.update(total_memory=memory_data.total,
                         available=memory_data.available,
                         percent=memory_data.percent,
                         free=memory_data.free)
    return memory_result


def process_info():
    process_result = {}
    process_data = psutil.Process()
    process_result.update(name=process_data.name(),
                          exe=process_data.exe(),
                          status=process_data.status(),
                          create_time=process_data.create_time())
    return process_result


def disk_info():
    disk_result = {}
    disk_data = psutil.disk_usage('/')
    disk_result.update(total=float(disk_data.total),
                       used=disk_data.used,
                       free=disk_data.free,
                       percent=disk_data.percent)
    return disk_result


def show(cpu, memory, process, disk):
    cpu_template = 'текущая частота процессора: {current_freq} Гц'
    memory_template = ('общая память: {total_memory} б \n'
                       'доступная память: {available} б \n'
                       'процент использования памяти:{percent}% \n'
                       'свободная память: {free} б')
    process_template = ('имя процесса: {name} \n'
                        'путь к исполняемому файлу: {exe} \n'
                        'статус процесса: {status} \n'
                        'время создания процесса: {create_time} мс')
    disk_template = ('информация об общей памяти диска: {total} б \n'
                     'информация об использованной памяти диска: {used} б \n'
                     'информация о свободной памяти диска: {free} б \n'
                     'использованная память в процентах: {percent}%')

    print('Информация о процессоре: ', cpu_template.format(**cpu), sep='\n', end='\n\n')
    print('Информация о памяти: ', memory_template.format(**memory), sep='\n', end='\n\n')
    print('Информация о процессах: ', process_template.format(**process), sep='\n', end='\n\n')
    print('Информация о батарее: ', disk_template.format(**disk), sep='\n', end='\n\n')


def main():
    cpu_data = cpu_info()
    memory_data = memory_info()
    process_data = process_info()
    disk_data = disk_info()
    show(cpu=cpu_data, memory=memory_data, process=process_data, disk=disk_data)


if __name__ == '__main__':
    main()
