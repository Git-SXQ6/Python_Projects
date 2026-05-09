# Group Number: Group 9  
# Group Project: Bug Report  


### Example

For the purposes of this exercise, a bug is anything in the code that could cause the program to behave incorrectly under normal operation. Bugs don't include things that are clunky or poorly designed, but functional.

| No | Bug Description | Suggested Fix | Difficulty to Fix (easy, medium, hard) | Priority (low, medium, high) |
|----|----------------|---------------|----------------------------------------|-------------------------------|
| 1  | If the user clicks “save” without entering any data, the app crashes | Disable save button unless all fields are filled in and then enable it when there is data to save | Medium | High |
| 2  | The “close” button doesn't actually close the program | Add the close action to the close button | Easy | Low |

_**You should not add extra rows to the form. Any extra rows will be disregarded.**_

#### We can find as many bugs as possible, and get rid of the less important ones at the end

**Task allocation:**
- Poster: Adi
- Statistics: Mohamed
- Visualisation: Siqi
- Data Logic & Integration: Xiaoqian & Defne




| No | Bug description | Suggested fix | Difficulty (easy/medium/hard) | Priority (low/medium/high) |
|----|-----------------|--------------|-------------------------------|----------------------------|
| 1  |(data_handler.py) CSV was not loaded on start-up (load_from_cvs() was commented out)               |Uncomment self.data - self.load_from.csv()              |Easy                               |High (well, the file does not open)                           |
| 2  |(data_handler.py) filter_by_ticket() uses != instead of == (which is inverted logic) ie., it return everyone except the ones that have the ticket                 |Replace != to ==               |Easy                               |High                            |
| 3  |(data_handler.py) ticket format mismatch with with DH and CSV file                 |The fix is by extracting the day number from the day string and rebuilds it in the correct format - by adding these lines under return self.data -> day_number = day.split()[1] AND under that day_ticket = f"{day_number} Day"      |Medium                               |High (code still runs but with a completely broken gig eligibility behaviour)                         |
| 4  |(data_handler.py) change data type for age and distance|       add int() & float()       |               Easy                |            determine after checking with visualisation                |
| 5  |        (data_handler.py) change data type in function         |      add int() & float()        |           Easy                    |            determine after checking with visualisation                |
| 6  |        (poster.py) incorrect for loop iteration: the code uses .values() to loop through the gigs dictionary which only returns the list of bands. However, the for loop is created to get the values for two variables - day and gigs.          |        CHange .values() to .items() so that both the day variable and band name is returned together for each iteration      |                 Easy              |             High               |
| 7  |      (poster.py) the text is added in the wrong position in the new window, all text is positioned at x = 500 with anchor=tk.NW which leaves the left half of the poster empty           |        To position the text at the center of the poster, x position should be set to 400 (given window size of 800) and anchor=tk.CENTER      |                   Easy            |                Low (code will still run)            |
| 8  |(data_handler.py)Adjust function: get_eligible_festival_goers()|differentiate between ticket type and the days they come|               Medium                |            High                |
| 9  |(data_handler.py) make sure the software can read festival_goers.csv info|Always find csv file from the folder that data_hander.py is in: import os\n base_dir = os.path.dirname(os.path.abspath(__file__))\n self.filename = os.path.join(base_dir, filename)|Easy|             Medium(can achieve by forcing everyone to open this code in festival_app directory, but thats kind of inflexible)               |
| 10 |(data_handler.py)Remove duplicate data points in csv file|add new function|               medium                |               High (otherwise introduce error in statistics)             |
| 11 |(Visualisation.py)Statistics clears the whole graph area, including the pie chart, graph buttons, and Back button. This happens because graph and statistics share the same right_frame, and show_statistics() destroys all widgets in that frame.                 |Put graph and statistics into separate frames, or make show_statistics() clear only its own statistics container.              |Medium                               |High                            |
| 12 |(Visualisation.py) No empty-data check before drawing the pie chart. If a ticket type has no attendees, update_graphs() still calls ax.pie() with empty data.                 |Add if not distribution: before plotting, and show a message such as “No data available”.              |Easy                               |High                            |
| 13 |(Visualisation.py) Add if not distribution: before plotting, and show a message such as “No data available”.                 |Remove or hide only the chart canvas, not visualization.parent.              |Easy                               |Medium                            |
| 14 |(Visualisation.py) Old chart widget is destroyed, but the old Matplotlib figure is not explicitly closed. This may cause unnecessary memory use after repeated updates.                 |Store the figure as self.figure and call plt.close(self.figure) before creating a new one.             |Medium                               |Low                            |
| 15 |in csv file there is a row named 12 - how to filter correct name input|              |                               |                            |
| 16 |in csv file there is a row that repeated title|              |                               |                            |
| 17 |visualization - cannot return to graph visualization after show festival statistics|              |                               |                            |
| 18 |poster - 'show festival poster' button does not work|              |                               |                            |
| 19 |data-handler - auto-detect duplicate festival goer input|              |                               |                            |
| 20 |poster - show list of gigs for each day on poster?|              |                               |                            |
| 21 |statsistics_handler - treats 0 as false                 |validate inputs as valid or invalid              |easy                               |High                            |
| 22 |statistics_handler - if df is empty, causes a runtime crash                 |add a check to ensure dataset is not empty before performing the devision              |easy                               |High                            |
| 23 |                 |              |                               |                            |
| 24 |                 |              |                               |                            |
| 25 |                 |              |                               |                            |
| 26 |                 |              |                               |                            |
| 27 |                 |              |                               |                            |
| 28 |                 |              |                               |                            |
| 29 |                 |              |                               |                            |
| 30 |                 |              |                               |                            |
| 31 |                 |              |                               |                            |
| 32 |                 |              |                               |                            |
| 33 |                 |              |                               |                            |
| 34 |                 |              |                               |                            |
| 35 |                 |              |                               |                            |
| 36 |                 |              |                               |                            |
| 37 |                 |              |                               |                            |
| 38 |                 |              |                               |                            |
| 39 |                 |              |                               |                            |
| 40 |                 |              |                               |                            |



