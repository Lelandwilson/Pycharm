import os
if __name__ == '__main__':

    command = "echo \"CPU `LC_ALL=C top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\\1/\"" \
              " | awk '{print 100 - $1}'`% RAM `free -m | awk '/Mem:/ { printf(\"%3.1f%%\", $3/$2*100) }'`" \
              " HDD `df -h / | awk '/\// {print $(NF-1)}'`\""
    Stats = str(os.popen(command).readline())

    print("\n" + Stats)

    command = "vcgencmd measure_temp"
    Temp = str(os.popen(command).readline())
    print(Temp)

    command = "ps -eo pid,ppid,cmd,comm,%mem,%cpu --sort=-%mem | head -10"
    process = ""
    # for line in str(os.popen(command).readline()):
    # process+= line
    process = str(os.popen(command).read())
    print(process)

