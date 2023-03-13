/******************************************************************************
 * USER SETTINGS
 *****************************************************************************/

// Display names & screen indices
// Remember, screen index starts at 0!

// Display name where answer is recorded
var TRIAL_DISPLAY = 'Trial';

// Screen index where answer is recorded
var TRIAL_SCREEN = 3;

// Display name where bonus is shown
var BONUS_DISPLAY = 'End';

// Screen index where bonus is shown
var BONUS_SCREEN = 1;



// ----------------------------------------------------------------------------

// Other vars

// Name of embedded variable where response is stored; this is set under
// Task Structure on display TRIAL_DISPLAY and screen TRIAL_SCREEN
var EMBEDDED_RESPONSE = 'responseVar';

// Formatted string for bonus payment amount
var BONUS_PAYMENT = '$10';

// HTML to display if participant got a bonus
var BONUS_HTML_Y = '<span class="centered">'
    + '<h1>'
    + 'Congratulations! You will receive a bonus of '
    + BONUS_PAYMENT + '.'
    + '</h1>'
    + '<p>'
    + 'Please allow up to 3 business days for processing.'
    + '</p>'
    + '</span>';

// HTML to display if participant did not get a bonus
var BONUS_HTML_N = '<h2 class="centered">'
    + 'Your response was incorrect in the randomly selected '
    + 'trial, so you will not receive a bonus payment.'
    + '</h2>';

// Placeholders for randomized stimuli
var blues = [];
var reds = [];
var sanityblues = [];
var sanityreds = [];



/******************************************************************************
 * CODE
 *****************************************************************************/

gorillaTaskBuilder.preProcessSpreadsheet((spreadsheet: any[]) => {

    // Set a seed.
    var randomSeed = gorilla.retrieve('randomSeedKey', null, true);
    if(!randomSeed){
        randomSeed = Date.now();
        gorilla.store('randomSeedKey', randomSeed, true);
    }

    // Collect all of the images from the spreadsheet, collate them, and randomize the order.
    for(var i = 0; i<spreadsheet.length; i++) {
        // For each spreadsheet row, we want check our image set column and store any non-empty entries
        if(spreadsheet[i]['blueStimulus'] != '') {
            blues.push(spreadsheet[i]['blueStimulus']); 
        } 
        if(spreadsheet[i]['redStimulus'] != '') { 
            reds.push(spreadsheet[i]['redStimulus']); 
        }
        if(spreadsheet[i]['sanityBlueStimulus'] != '') { 
            sanityblues.push(spreadsheet[i]['sanityBlueStimulus']); 
        }
        if(spreadsheet[i]['sanityRedStimulus'] != '') { 
            sanityreds.push(spreadsheet[i]['sanityRedStimulus']); 
        }
    }
    blues = gorilla.shuffle(blues, randomSeed);
    reds = gorilla.shuffle(reds, randomSeed);
    sanityblues = gorilla.shuffle(sanityblues, randomSeed);
    sanityreds = gorilla.shuffle(sanityreds, randomSeed);

    // Procedurally build our spreadsheet
    var modifiedSpreadsheet = [];
    var trialCounter = 0;
    var blockCounter = 0;
    var bluesCounter = 0;
    var redsCounter = 0;
    var sanitybluesCounter = 0;
    var sanityredsCounter = 0;
    for(var i = 0; i<spreadsheet.length; i++) {
        var currentRow = spreadsheet[i];
        // At the start of a block, shuffle the order of the stimuli
        if (currentRow.display == "Block1" || currentRow.display == "Block2" || currentRow.display == "Block3" || currentRow.display == "Block4") {
            blockCounter++;
        }
        // Add in the shuffled stimuli
        if (currentRow.display == "Trial") {
            if (currentRow.sanity == 0) {
                if (currentRow.ANSWER == "left") { 
                    currentRow.stimulus = blues[bluesCounter]; 
                    bluesCounter++;
                } else {
                    currentRow.stimulus = reds[redsCounter]; 
                    redsCounter++;
                }
            } else {
                if (currentRow.ANSWER == "left") { 
                    currentRow.stimulus = sanityblues[sanitybluesCounter]; 
                    sanitybluesCounter++;
                } else {
                    currentRow.stimulus = sanityreds[sanityredsCounter]; 
                    sanityredsCounter++;
                }
            }
            currentRow.block = blockCounter;
            trialCounter++;
            currentRow.trial = trialCounter;
        }
        modifiedSpreadsheet.push(currentRow);
    }
    return modifiedSpreadsheet;
});



gorillaTaskBuilder.onScreenStart((spreadsheet: any, rowIndex: number, screenIndex: number, row: any, container: string) => {

    // Select random bonus and display result at end of task
    if (row.display == BONUS_DISPLAY && screenIndex == BONUS_SCREEN) {
        var allResponses = gorilla.retrieve('allResponses', [], true);
        var allScores = gorilla.retrieve('allScores', [], true);
        var randomTrial = Math.floor(Math.random() * allResponses.length);
        var randomResult = allResponses[randomTrial];
        var randomScore = allScores[randomTrial];
        if (randomScore) {
            $(container + ' .content').html(BONUS_HTML_Y);
        } else {
            $(container + ' .content').html(BONUS_HTML_N);
        }
        gorilla.refreshLayout(); // Recalculate page layout with our new HTML
        // Store the bonus details in the task data
        gorilla.metric({
            response_type: 'Bonus Trial',
            response: randomTrial + 1
        });
        gorilla.metric({
            response_type: 'Bonus Correct',
            response: randomScore
        });
        gorilla.metric({
            response_type: 'Bonus Response',
            response: randomResult
        });
    }

});



gorillaTaskBuilder.onScreenFinish((spreadsheet: any, rowIndex: number, screenIndex: number, row: any, container: string, correct: boolean) => {

    // Store each response at the end of the response screen
    // including timeouts/no response
    if (row.display == TRIAL_DISPLAY && screenIndex == TRIAL_SCREEN) {
        var lastResponse = gorilla.retrieve(EMBEDDED_RESPONSE, null, true);
        var allResponses = gorilla.retrieve('allResponses', [], true);
        allResponses.push(lastResponse);
        gorilla.store('allResponses', allResponses, true);
        var allScores = gorilla.retrieve('allScores', [], true);
        allScores.push(lastResponse == row.ANSWER);
        gorilla.store('allScores', allScores, true);
    }
    
    // Calculate practice accuracy
    if (row.display == "Practice" && screenIndex == 3) {
        var practice_correct = gorilla.retrieve('practice_correct', null, true);
        var practice_total = gorilla.retrieve('practice_total', null, true);
        var practice_accuracy = Math.floor((practice_correct/practice_total)*100)
        gorilla.store('practice_accuracy', practice_accuracy, true);
    }
    
    // Reset practice embeded data if "Retry"
    if (row.display == "PracticeEnd" && screenIndex == 1) {
        gorilla.store('practice_correct', 0, true);
        gorilla.store('practice_total', 0, true);
    }
    
});