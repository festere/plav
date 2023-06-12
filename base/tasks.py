from __future__ import absolute_import, unicode_literals
from celery import shared_task
from PlateformeAntivirale.celery import app
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils import html
import os
from colorama import Fore
import docker
import re
import subprocess
import random
import time
import calendar
from celery import group

#------------------------------
# ANSI character remover
#------------------------------
def remove_ansi_escape_codes(log_string):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', log_string)


#------------------------------
# Remove a file if it exists since more than 5 minutes
#------------------------------
def tmp_cleaner():
    folder_path = 'tmp'
    
    try:
        files = os.listdir(folder_path)
        current_time = time.gmtime() # Get today's date
        timestamp = calendar.timegm(current_time) # Transform today's date to a timestamp

        for file_name in files:
            file_path = os.path.join(folder_path, file_name) # Get the file path of each elements in the /tmp
            try:
                creation_time = os.path.getctime(file_path) # Get the import date of each elements in the /tmp

                runing_time = timestamp - creation_time

                if runing_time > 300:
                    os.remove(file_path)
                    print(Fore.GREEN + "The file: " + Fore.RESET + file_name + Fore.GREEN + " is here since more than 5 minutes and has been deleted" + Fore.RESET)
            except OSError:
                print(Fore.GREEN + "An error occurred while retrieving the creation time for file " + Fore.RESET  + file_name)

    except OSError:
        print(f"Unable to list files in folder '{folder_path}'.")


#------------------------------
# Remove a docker container if it exited
#------------------------------
def container_cleaner():
    client = docker.from_env()
    containers = client.containers.list(all=True)

    for container in containers:
        if container.status == "exited":
            subprocess.check_output('docker rm ' + container.id, shell=True)
            print(f"Container Status: {container.status}")


#------------------------------
# ClamAV container
#------------------------------
@app.task
def start_clamav_container(file_path):
    name = 'clamav' + str(random.randint(0,9999999999))
    try:
        subprocess.check_output('sudo docker stop ' + name + '&& docker rm ' + name, shell=True)
        print(Fore.RED + "A container has been left runnig but has been terminated" + Fore.RESET)
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "ClamAV" + Fore.RESET)
    except:
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "ClamAV" + Fore.RESET)

    client = docker.from_env()
    container_ClamAV = client.containers.run(
        image='festere/clamav:latest',
        name=name,
        volumes={file_path: {'bind': '/data', 'mode': 'rw'}},
        command='clamscan /data',
        detach=True,
    )

    result_ClamAV = ""
    print(Fore.GREEN + "From: "+ Fore.RED + "ClamAV " + Fore.GREEN + "Result: " + Fore.RESET)
    for line in container_ClamAV.logs(stream=True):
        decoded_line = line.decode('utf-8').strip()
        print(decoded_line)
        cleaned_line = remove_ansi_escape_codes(decoded_line)
        escaped_line = html.escape(cleaned_line)
        result_ClamAV += escaped_line + "\n"

    container_ClamAV.stop()
    container_ClamAV.remove()
    return result_ClamAV


#------------------------------
# Comodo container
#------------------------------
@app.task
def start_comodo_container(file_path):
    name = 'comodo' + str(random.randint(0,9999999999))
    try:
        subprocess.check_output('sudo docker stop ' + name + '&& docker rm ' + name, shell=True)
        print(Fore.RED + "A container has been left runnig but has been terminated" + Fore.RESET)
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "Comodo" + Fore.RESET)
    except:
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "Comodo" + Fore.RESET)

    client = docker.from_env()
    container_Comodo = client.containers.run(
        image='festere/comodo:latest',
        name=name,
        volumes={file_path: {'bind': '/data', 'mode': 'rw'}},
        command='opt/COMODO/./cmdscan -s /data -v',
        detach=True,
    )

    result_Comodo = ""
    print(Fore.GREEN + "From: "+ Fore.RED + "Comodo " + Fore.GREEN + "Result: " + Fore.RESET)
    for line in container_Comodo.logs(stream=True):
        decoded_line = line.decode('utf-8').strip()
        print(decoded_line)
        cleaned_line = remove_ansi_escape_codes(decoded_line)
        escaped_line = html.escape(cleaned_line)
        result_Comodo += escaped_line + "\n"

    container_Comodo.stop()
    container_Comodo.remove()
    return result_Comodo


#------------------------------
# RKhunter
#------------------------------
@app.task
def start_rkhunter_container(file_path):
    name = 'rkhunter' + str(random.randint(0,9999999999))
    try:
        subprocess.check_output('sudo docker stop ' + name + '&& docker rm ' + name, shell=True)
        print(Fore.RED + "A container has been left runnig but has been terminated" + Fore.RESET)
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "RKhunter" + Fore.RESET)
    except:
        print(Fore.GREEN + "Analysis of: " + Fore.RESET + file_path + Fore.GREEN + " by: " + Fore.RED + "RKhunter" + Fore.RESET)

    client = docker.from_env()
    container_RKhunter = client.containers.run(
        image='festere/rkhunter',
        name=name,
        volumes={file_path: {'bind': '/data', 'mode': 'rw'}},
        command='rkhunter -c -q --skip-keypress --nocolors --summary',
        detach=True,
    )

    result_RKhunter = ""
    print(Fore.GREEN + "From: "+ Fore.RED + "rkhunter " + Fore.GREEN + "Result: " + Fore.RESET)
    for line in container_RKhunter.logs(stream=True):
        decoded_line = line.decode('utf-8').strip()
        print(decoded_line)
        cleaned_line = remove_ansi_escape_codes(decoded_line)
        escaped_line = html.escape(cleaned_line)
        result_RKhunter += escaped_line + "\n"


    container_RKhunter.stop()
    container_RKhunter.remove()
    return result_RKhunter


#------------------------------
# Main file upload handler
#------------------------------
@shared_task
def upload_file(request):
    # Get the context from the request
    if request.method == 'POST':
        uploaded_file = request.FILES['fileToUpload']
        uploaded_file_original = uploaded_file.name
        print(Fore.GREEN + "File uploaded: " + Fore.RESET + uploaded_file.name)

        uploaded_file.name = re.sub(r'à', 'a', uploaded_file.name) # Replace the "à" by "a"
        uploaded_file.name = re.sub(r'â', 'a', uploaded_file.name) # Replace the "â" by "a"
        uploaded_file.name = re.sub(r'ä', 'a', uploaded_file.name) # Replace the "ä" by "a"

        uploaded_file.name = re.sub(r'é', 'e', uploaded_file.name) # Replace the "é" by "e"
        uploaded_file.name = re.sub(r'è', 'e', uploaded_file.name) # Replace the "è" by "e"
        uploaded_file.name = re.sub(r'ê', 'e', uploaded_file.name) # Replace the "ê" by "e"
        uploaded_file.name = re.sub(r'ë', 'e', uploaded_file.name) # Replace the "ë" by "e"

        uploaded_file.name = re.sub(r'î', 'i', uploaded_file.name) # Replace the "î" by "i"
        uploaded_file.name = re.sub(r'ï', 'i', uploaded_file.name) # Replace the "ï" by "i"

        uploaded_file.name = re.sub(r'ô', 'o', uploaded_file.name) # Replace the "ô" by "o"
        uploaded_file.name = re.sub(r'ö', 'o', uploaded_file.name) # Replace the "ö" by "o"

        uploaded_file.name = re.sub(r'ù', 'u', uploaded_file.name) # Replace the "ù" by "u"
        uploaded_file.name = re.sub(r'û', 'u', uploaded_file.name) # Replace the "û" by "u"
        uploaded_file.name = re.sub(r'ü', 'u', uploaded_file.name) # Replace the "ü" by "u"

        uploaded_file.name = re.sub(r'ÿ', 'y', uploaded_file.name) # Replace the "ÿ" by "y"
        uploaded_file.name = re.sub(r'ŷ', 'y', uploaded_file.name) # Replace the "ŷ" by "y"

        uploaded_file.name = re.sub(r'ç', 'c', uploaded_file.name) # Replace the "ç" by "c"

        uploaded_file.name = re.sub(r'[^\w./]+', '', uploaded_file.name) # Remove the accents on other letters
        uploaded_file.name = re.sub(r'[^\x00-\x7F]+', '', uploaded_file.name) # Remove the space

        print(Fore.GREEN + "File renamed: " + Fore.RESET + uploaded_file.name)


        # Get the full path to the directory where uploaded file is to be saved
        save_directory = os.path.join('tmp')
        os.makedirs(save_directory, exist_ok=True) # Create a tmp/ folder if it doesn't exist
        file_path = os.path.abspath(os.path.join(save_directory, uploaded_file.name + str(random.randint(0,9999999999))))
        print(Fore.GREEN + "File placed at: " + Fore.RESET + file_path)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

            tmp_cleaner()
            container_cleaner()

            task_group = group(
                start_clamav_container.si(file_path),
                start_comodo_container.si(file_path),
                start_rkhunter_container.si(file_path)
            )
        result_group = task_group.apply_async()
        result_ClamAV, result_Comodo, result_RKhunter = result_group.get()

        # Return a response indicating success
        print(Fore.GREEN + "Successful analysis of: " + Fore.RESET + file_path + Fore.RESET)
        try:
            return render(request, 'upload_success.html', {'uploaded_file': uploaded_file_original,
                                                       'result_ClamAV': result_ClamAV,
                                                       'result_Comodo': result_Comodo,
                                                       'result_RKhunter' : result_RKhunter,
                                                       })
        except OSError:
            print(Fore.RED + "Can't start the upload_success page" + Fore.RESET)

    else:
        # Render the file upload form
        print(Fore.RED + "Unseccessful analysis at: " + Fore.RESET + file_path + Fore.GREEN + " with file name: " + Fore.RESET + uploaded_file.name)
        return render(request, 'home.html')
