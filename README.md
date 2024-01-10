<!-- ABOUT -->
## About

A simple python script to make a periodic backup of a given folder. For practice purposes, the shutil module was avoided.


<!-- GETTING STARTED -->
## Getting Started

You may simply download the synch_folders.py file or clone the repo and follow the instructions below.



<!-- USAGE EXAMPLES -->
## Usage

To use the script you need only call the file with four arguments:
1) the path to the folder you wish to backup
2) the path to the backup folder (creates folder if none exists)
3) the file that logs the changes (creates file if none exists)
4) the interval for the iteration of the script - the default unit of time is seconds, but with the flag -u it may be read as minutes (-um), hours (-uh), or days (-ud)

Linux command line example: $ python3 synch_folders.py /path/to/sourceFolder/ /path/to/replicaFolder/ logFile.log 30 -u<b>m</b>

This will synch the replica folder with the source folder every 30 <b>m</b>inutes

See the [open issues](https://github.com/LCGhit/folder_synchronization/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Thank you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Luís Cunha - luispcunha@proton.me

Project Link: [https://github.com/LCGhit/folder_synchronization](https://github.com/LCGhit/folder_synchronization)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
