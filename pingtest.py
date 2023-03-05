import subprocess


def ping(host):
    # Run the ping command and capture the output
    output = subprocess.Popen(['ping', '-n', '1', host], stdout=subprocess.PIPE).communicate()[0]

    # Parse the output
    output = output.decode('windows-1252')
    output = output.split('Moyenne = ')[1]
    output = output.split('ms')[0]
    print(output)
    return output


