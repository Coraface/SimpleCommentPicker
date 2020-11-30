# SimpleCommentPicker

A simple program in python to run a simulation of a Comment Picker and test results. <br>
You choose how many lifetimes you want to try winning giveaways, participants and giveaways. <br>
Probability formulas where taken from <b>Vsauce2</b> youtube channel. <br>
The program runs in parallel, using multiprocessing. <br><br>
Change the following values according to your needs: <br>
* <b>NUM_OF_LIVES</b>: the number of lifetimes
* <b>NUM_OF_USERS</b>: the number of participants for each giveaway
* <b>GIVEAWAYS</b>: the number of giveaways for each lifetime

<b><i>Tips</i></b>
* More processes = faster runtime
* Don't use too many processes, unless your computer can handle it
* Make sure NUM_OF_LIVES / processes != float
* To run sequentially, use <i>"procs = 1"</i>
