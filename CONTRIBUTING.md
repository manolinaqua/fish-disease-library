exam# Instructions for Contributing

The instructions here assume that you have already created a github account of your own. If you have not simply go to [github](https://github.com) and make an account.

## Pre-requisites

All downloads are free and don't require payment.

1. Download the [github desktop application](https://github.com/apps/desktop) (ideal if non technical)
	- For technical folks, you can of course utilize the Github CLI if that is more your preference.
2. Download [Obsidian](https://obsidian.md/download), a powerful note taking application which is used to structure and power the library.
    - We recommend using your computer for this and not the mobile version of the application.
    - While these files are `markdown` we utilize a number of features unique to Obsidian like tags, links and search that we are in the final application.
## Setting things up

#### Step 1: Fork the repository
- Navigate to the [fish-disease-libary](https://github.com/manolinaqua/fish-disease-library) repository in your browser and click the arrow next to *fork* to open the menu and select "*Create a new fork*".
![Forking a repo](./imgs/fork.png)

#### Step 2: Clone the repository
- Clone your newly forked version of the repository onto your computer. 
	- You can find instructions on how to [clone your repository here](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)
		- Copy the HTTPS format
		- Press Clone, if you are happy where the folder sits on your computer - change it if not then press Clone

#### Step 3: Open the repository in Obsidian
- When you open Obsidian you should see an option to **Open folder as vault**. Click it.
![Obsidian Start Page](./imgs/obsidian_start.png)
- When the file system explorer pops up navigate to the `/fish-disease-library` folder.
- **Important:** Before hitting Select make sure you have the `Fish Disease Libary` selected. So the final vault location should be `<your file system>/fish-disease-library/Fish Disease Library`
	- If this step is not followed then links will not update appropriate.

#### You are now set up and ready to contribute!
- Your Obsidian vault should look exactly the same as the [Fish Disease Library website](https://fishdiseases.manolinaqua.com/welcome.html). 
- Your Github desktop should be empty (*if not see picture below)*. 
	- As you edit in Obsidian the files changed will be listed on the left and the exact text changes on the right.
	- 'Current branch' should be Main.

If it looks like this, right click on the orange dot and 'Dismiss Changes'
![[Example of phantom changes.png]]




## Editing, committing and making pull requests
First, comment or open a new Issue on the [Github website](https://github.com/manolinaqua/fish-disease-library/issues) to say what you are working on and a estimated timeline. This is to coordinate and try avoid two people working on the same thing. If you are unsure, just comment or ask on the issue and someone will comment back.

#### Step 4: Making edits in Obsidian
- Simply start typing and making your changes. You can 'Cmd /Ctrl Z' if you want to go back
- Obsidian **useful tips and tricks:**
	- Use [ ] brackets immediately followed by ( ) for in text references with the weblink 
	- Use [[]] double brackets when mentioning another disease in the library, in order to link to that disease e.g [[Moritella Viscosa]]
	- Find and 'Replace' is found under the 3 dots (...) option in the top right corner
	- For further tips about Obsidian have a look at [this tutorial]([https://www.youtube.com/watch?v=z4AbijUCoKU](https://www.youtube.com/watch?v=z4AbijUCoKU)
- If it’s been a few days since your last edit, use “Fetch origin” in GitHub Desktop to pull in any updates to existing files.
	- **Note:** new diseases or sections will not update then you need to [sync fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork). You can see this by going to the [Fish Disease Library website](https://fishdiseases.manolinaqua.com/welcome.html) to see if there are new sections.

#### Step 5: "Commit" your work

- To get your updates into **Github** you need perform a "commit" from Github desktop
- You'll see your changed files (pictured), then simply write a title e.g 'Update of *disease name*' and short description of the changes you made. 
- Press the blue **commit file to main** button.
	- Learn more about commits [here](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop#write-a-commit-message-and-push-your-changes)
 ![[commit.png]]

- Then click the blue '**Push origin'** button on the right (pictured)

![[Example pushing changes to Git website.png]]


- This puts your changes on the public GitHub, but to draw attention and get your changes approved to go live in the library, you need to make a Pull Request when you are finished.

#### 6. Create a pull request in GitHub

- After you've made your edits, go to the GitHub webpage and click on your profile in the top right hand corner. This is your fork of the fish disease library on the github webpage (pictured). It is a link like the one below
	- `https://github.com/<your user name>/fish-disease-library`
- Notice the commits you have made are there, click 'Contribute' then 'Open pull Request'

![[Example opening a PR request.png]]

- You should then see a menu similar to below. Make sure that the **base repository: manolinaqua/fish-disease-library** is selected on the left drop down.
	- If there are conflicts (for example if you had not 'fetch origin' and the file you were working on was already changed by someone else), then you will need to go through and resolve conflicts.
![Pull Info](./imgs/pull_branch.png)
- Then simply add a brief title stating what you did and follow the template in the description.
	- Marking the [ ] boxes with an X (you might need to remove a space)
	- Make sure to add the link of the issue you were addressing
- Once complete click the **Create pull request** button, sit back, and wait for someone to review it!

More information on Github's pull request process can be found here. [Example](https://docs.github.com/en/get-started/start-your-journey/hello-world)

