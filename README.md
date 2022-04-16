<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />

<div align="center">
  <a href="https://github.com/msrogers2015/Just-Enough-Git">
    <img src="img/git.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Just Enough Git</h3>

  <p align="center">
    GUI with just enough Git to create a repo and commit it to github with branch support
    <br />
    <a href="https://github.com/msrogers2015/Just-Enough-Git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/msrogers2015/Just-Enough-Git/issues">Report Bug</a>
    ·
    <a href="https://github.com/msrogers2015/Just-Enough-Git/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I recently started focusing on working on my own projects and what was a better first large-ish scale project than creating a GUI for git?! Rather than recreating the wheel, I decided to focus on those, who like me, are intemidated by (C)ommand (L)ine (I)nterface tools.

All of the git options are seperated into menu options at the top of the app (typically where youd see save, open, things of that nature) and create their own dialog box when information needs to be passed with the exception of full commit messages. The goal is to impliment enough of git that any new user can get started quickly and have enough at their disposal to work on a single person project.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/) using only built in packages
* [Git](https://git-scm.com/) for all the hard work in the background

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Only thing you need is python and git installed. I will warn you to check your tkinter install, it seems that sometimes it's not installed and youd need to install it yourself (i believe it's an option in the python installer that needs to be selected when first installing python.)

### Installation

1. Ensure git and python is installed via their installers. 
2. Clone the repo
   ```sh
   git clone https://github.com/msrogers2015/Just-Enough-Git.git
   ```
3. Run the main.py file from a terminal
   ```sh
   python main.py
   ```
   Alternatively double click the run.bat file (do not move this file as it is path dependent)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

From the Setup menu you can start or downlaod git repos. You also have the ability yo change the information displayed on github when you push a git( name and email)
The Staging menu allows you to add and remove files form the stage as well as get the current status and see changes and commit your changes. The branches menu allow users to switch between branches. Lastly the Update menu updates your local repo by allowing you to pull adn getch or update remote repo by pushing your commits 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Init and Clone Repos
- [x] Update User Info (Name and Email)
- [x] Get Status
- [x] Stage/Unstage files
    - [x] Show unstaged file history
- [x] Full Commit
    - [x] Quick Commit
- [x] List Branches
- [x] Create Branch
- [x] Switch Branches
- [x] Merge Branches
- [ ] Commit History
    - [ ] Compare Commits
    - [ ] Compare Changes
- [ ] Fetch command
- [x] Pull command
- [ ] Merge command
- [x] Push command

See the [open issues](https://github.com/msrogers2015/Just-Enough-Git/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Since this is my first project I would like to keep contributing closed but I do plan on creating a full featured version with all the additional git commands such as rebase, allowing the switching between merge types (i.e three way merge), etc. There is currently an empty repo for this named [Get Good with Git](https://github.com/msrogers2015/Get-Good-with-Git).

If you have a suggestion that would make this better, please open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Marquel Rogers  - rogersmar2015@gmail.com

Project Link: [https://github.com/msrogers2015/Just-Enough-Git](https://github.com/msrogers2015/Just-Enough-Git)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/msrogers2015/Just-Enough-Git.svg?style=for-the-badge
[contributors-url]: https://github.com/msrogers2015/Just-Enough-Git/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/msrogers2015/Just-Enough-Git.svg?style=for-the-badge
[forks-url]: https://github.com/msrogers2015/Just-Enough-Git/network/members
[stars-shield]: https://img.shields.io/github/stars/msrogers2015/Just-Enough-Git.svg?style=for-the-badge
[stars-url]: https://github.com/msrogers2015/Just-Enough-Git/stargazers
[issues-shield]: https://img.shields.io/github/issues/msrogers2015/Just-Enough-Git.svg?style=for-the-badge
[issues-url]: https://github.com/msrogers2015/Just-Enough-Git/issues
[license-shield]: https://img.shields.io/github/license/msrogers2015/Just-Enough-Git.svg?style=for-the-badge
[license-url]: https://github.com/msrogers2015/Just-Enough-Git/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/marquel-rogers/
[product-screenshot]: images/screenshot.png