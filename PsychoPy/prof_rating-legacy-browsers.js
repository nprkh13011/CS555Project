/******************** 
 * Prof_Rating *
 ********************/


// store info about the experiment session:
let expName = 'prof_rating';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
flowScheduler.add(Prof1RoutineBegin());
flowScheduler.add(Prof1RoutineEachFrame());
flowScheduler.add(Prof1RoutineEnd());
flowScheduler.add(Prof2RoutineBegin());
flowScheduler.add(Prof2RoutineEachFrame());
flowScheduler.add(Prof2RoutineEnd());
flowScheduler.add(Prof3RoutineBegin());
flowScheduler.add(Prof3RoutineEachFrame());
flowScheduler.add(Prof3RoutineEnd());
flowScheduler.add(Prof4RoutineBegin());
flowScheduler.add(Prof4RoutineEachFrame());
flowScheduler.add(Prof4RoutineEnd());
flowScheduler.add(Prof5RoutineBegin());
flowScheduler.add(Prof5RoutineEachFrame());
flowScheduler.add(Prof5RoutineEnd());
flowScheduler.add(Prof6RoutineBegin());
flowScheduler.add(Prof6RoutineEachFrame());
flowScheduler.add(Prof6RoutineEnd());
flowScheduler.add(Prof7RoutineBegin());
flowScheduler.add(Prof7RoutineEachFrame());
flowScheduler.add(Prof7RoutineEnd());
flowScheduler.add(Prof8RoutineBegin());
flowScheduler.add(Prof8RoutineEachFrame());
flowScheduler.add(Prof8RoutineEnd());
flowScheduler.add(Prof9RoutineBegin());
flowScheduler.add(Prof9RoutineEachFrame());
flowScheduler.add(Prof9RoutineEnd());
flowScheduler.add(Prof10RoutineBegin());
flowScheduler.add(Prof10RoutineEachFrame());
flowScheduler.add(Prof10RoutineEnd());
flowScheduler.add(Prof11RoutineBegin());
flowScheduler.add(Prof11RoutineEachFrame());
flowScheduler.add(Prof11RoutineEnd());
flowScheduler.add(Prof12RoutineBegin());
flowScheduler.add(Prof12RoutineEachFrame());
flowScheduler.add(Prof12RoutineEnd());
flowScheduler.add(Prof13RoutineBegin());
flowScheduler.add(Prof13RoutineEachFrame());
flowScheduler.add(Prof13RoutineEnd());
flowScheduler.add(Prof14RoutineBegin());
flowScheduler.add(Prof14RoutineEachFrame());
flowScheduler.add(Prof14RoutineEnd());
flowScheduler.add(Prof15RoutineBegin());
flowScheduler.add(Prof15RoutineEachFrame());
flowScheduler.add(Prof15RoutineEnd());
flowScheduler.add(Prof16RoutineBegin());
flowScheduler.add(Prof16RoutineEachFrame());
flowScheduler.add(Prof16RoutineEnd());
flowScheduler.add(Prof17RoutineBegin());
flowScheduler.add(Prof17RoutineEachFrame());
flowScheduler.add(Prof17RoutineEnd());
flowScheduler.add(ThankYouScreenRoutineBegin());
flowScheduler.add(ThankYouScreenRoutineEachFrame());
flowScheduler.add(ThankYouScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var text;
var keySpacebar;
var Prof1Clock;
var HaveYouTakenThisProf;
var imageProf1;
var imageYesButton;
var imageNoButton;
var mouse;
var Prof2Clock;
var HaveYouTakenThisProf_2;
var imageProf2;
var imageYesButton_2;
var imageNoButton_2;
var mouse_2;
var Prof3Clock;
var HaveYouTakenThisProf_3;
var imageProf3;
var imageYesButton_3;
var imageNoButton_3;
var mouse_3;
var Prof4Clock;
var HaveYouTakenThisProf_4;
var imageProf4;
var imageYesButton_4;
var imageNoButton_4;
var mouse_4;
var Prof5Clock;
var HaveYouTakenThisProf_5;
var imageProf5;
var imageYesButton_5;
var imageNoButton_5;
var mouse_5;
var Prof6Clock;
var HaveYouTakenThisProf_6;
var imageProf6;
var imageYesButton_6;
var imageNoButton_6;
var mouse_6;
var Prof7Clock;
var HaveYouTakenThisProf_7;
var imageProf7;
var imageYesButton_7;
var imageNoButton_7;
var mouse_7;
var Prof8Clock;
var HaveYouTakenThisProf_8;
var imageProf8;
var imageYesButton_8;
var imageNoButton_8;
var mouse_8;
var Prof9Clock;
var HaveYouTakenThisProf_9;
var imageProf9;
var imageYesButton_9;
var imageNoButton_9;
var mouse_9;
var Prof10Clock;
var HaveYouTakenThisProf_10;
var imageProf10;
var imageYesButton_10;
var imageNoButton_10;
var mouse_10;
var Prof11Clock;
var HaveYouTakenThisProf_11;
var imageProf11;
var imageYesButton_11;
var imageNoButton_11;
var mouse_11;
var Prof12Clock;
var HaveYouTakenThisProf_12;
var imageProf12;
var imageYesButton_12;
var imageNoButton_12;
var mouse_12;
var Prof13Clock;
var HaveYouTakenThisProf_13;
var imageProf13;
var imageYesButton_13;
var imageNoButton_13;
var mouse_13;
var Prof14Clock;
var HaveYouTakenThisProf_14;
var imageProf14;
var imageYesButton_14;
var imageNoButton_14;
var mouse_14;
var Prof15Clock;
var HaveYouTakenThisProf_15;
var imageProf15;
var imageYesButton_15;
var imageNoButton_15;
var mouse_15;
var Prof16Clock;
var HaveYouTakenThisProf_16;
var imageProf16;
var imageYesButton_16;
var imageNoButton_16;
var mouse_16;
var Prof17Clock;
var HaveYouTakenThisProf_17;
var imageProf17;
var imageYesButton_17;
var imageNoButton_17;
var mouse_17;
var ThankYouScreenClock;
var textThankYouMessage;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the Test!\n\nPlease press the spacebar to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keySpacebar = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Prof1"
  Prof1Clock = new util.Clock();
  HaveYouTakenThisProf = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf1', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof2"
  Prof2Clock = new util.Clock();
  HaveYouTakenThisProf_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_2',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf2', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image2.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_2', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_2', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof3"
  Prof3Clock = new util.Clock();
  HaveYouTakenThisProf_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_3',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf3', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image3.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_3', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_3', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof4"
  Prof4Clock = new util.Clock();
  HaveYouTakenThisProf_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_4',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf4', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image4.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_4', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_4', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_4.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof5"
  Prof5Clock = new util.Clock();
  HaveYouTakenThisProf_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_5',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf5', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image5.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_5', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_5', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_5.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof6"
  Prof6Clock = new util.Clock();
  HaveYouTakenThisProf_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_6',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf6', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image6.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_6', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_6', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof7"
  Prof7Clock = new util.Clock();
  HaveYouTakenThisProf_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_7',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf7', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image7.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_7', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_7', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_7 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_7.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof8"
  Prof8Clock = new util.Clock();
  HaveYouTakenThisProf_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_8',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf8', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image8.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_8', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_8', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_8 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_8.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof9"
  Prof9Clock = new util.Clock();
  HaveYouTakenThisProf_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_9',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf9', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image9.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_9', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_9', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_9 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_9.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof10"
  Prof10Clock = new util.Clock();
  HaveYouTakenThisProf_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_10',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf10', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image10.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_10', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_10', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_10 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_10.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof11"
  Prof11Clock = new util.Clock();
  HaveYouTakenThisProf_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_11',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf11', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image11.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_11', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_11', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_11 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_11.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof12"
  Prof12Clock = new util.Clock();
  HaveYouTakenThisProf_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_12',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf12', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image12.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_12', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_12', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_12 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_12.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof13"
  Prof13Clock = new util.Clock();
  HaveYouTakenThisProf_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_13',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf13', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image13.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_13', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_13', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_13 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_13.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof14"
  Prof14Clock = new util.Clock();
  HaveYouTakenThisProf_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_14',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf14', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image14.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_14', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_14', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_14 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_14.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof15"
  Prof15Clock = new util.Clock();
  HaveYouTakenThisProf_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_15',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf15', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image15.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_15', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_15', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_15 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_15.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof16"
  Prof16Clock = new util.Clock();
  HaveYouTakenThisProf_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_16',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf16', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image16.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_16', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_16', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_16 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_16.mouseClock = new util.Clock();
  // Initialize components for Routine "Prof17"
  Prof17Clock = new util.Clock();
  HaveYouTakenThisProf_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'HaveYouTakenThisProf_17',
    text: 'Have you taken a class with this Professor?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  imageProf17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageProf17', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/image17.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.5, 0.45],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  imageYesButton_17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageYesButton_17', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  imageNoButton_17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageNoButton_17', units : undefined, 
    image : 'C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.3)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_17 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_17.mouseClock = new util.Clock();
  // Initialize components for Routine "ThankYouScreen"
  ThankYouScreenClock = new util.Clock();
  textThankYouMessage = new visual.TextStim({
    win: psychoJS.window,
    name: 'textThankYouMessage',
    text: 'Thank you for your time!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _keySpacebar_allKeys;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeScreen' ---
    t = 0;
    WelcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('WelcomeScreen.started', globalClock.getTime());
    keySpacebar.keys = undefined;
    keySpacebar.rt = undefined;
    _keySpacebar_allKeys = [];
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(text);
    WelcomeScreenComponents.push(keySpacebar);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeScreen' ---
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *keySpacebar* updates
    if (t >= 0.0 && keySpacebar.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySpacebar.tStart = t;  // (not accounting for frame time here)
      keySpacebar.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySpacebar.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySpacebar.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySpacebar.clearEvents(); });
    }
    
    if (keySpacebar.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySpacebar.getKeys({keyList: ['space'], waitRelease: false});
      _keySpacebar_allKeys = _keySpacebar_allKeys.concat(theseKeys);
      if (_keySpacebar_allKeys.length > 0) {
        keySpacebar.keys = _keySpacebar_allKeys[_keySpacebar_allKeys.length - 1].name;  // just the last key pressed
        keySpacebar.rt = _keySpacebar_allKeys[_keySpacebar_allKeys.length - 1].rt;
        keySpacebar.duration = _keySpacebar_allKeys[_keySpacebar_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeScreen' ---
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('WelcomeScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keySpacebar.corr, level);
    }
    psychoJS.experiment.addData('keySpacebar.keys', keySpacebar.keys);
    if (typeof keySpacebar.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keySpacebar.rt', keySpacebar.rt);
        psychoJS.experiment.addData('keySpacebar.duration', keySpacebar.duration);
        routineTimer.reset();
        }
    
    keySpacebar.stop();
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var Prof1Components;
function Prof1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof1' ---
    t = 0;
    Prof1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof1.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof1Components = [];
    Prof1Components.push(HaveYouTakenThisProf);
    Prof1Components.push(imageProf1);
    Prof1Components.push(imageYesButton);
    Prof1Components.push(imageNoButton);
    Prof1Components.push(mouse);
    
    Prof1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function Prof1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof1' ---
    // get current time
    t = Prof1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf* updates
    if (t >= 0.0 && HaveYouTakenThisProf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf.setAutoDraw(false);
    }
    
    // *imageProf1* updates
    if (t >= 0.0 && imageProf1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf1.tStart = t;  // (not accounting for frame time here)
      imageProf1.frameNStart = frameN;  // exact frame index
      
      imageProf1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf1.setAutoDraw(false);
    }
    
    // *imageYesButton* updates
    if (t >= 0.0 && imageYesButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton.tStart = t;  // (not accounting for frame time here)
      imageYesButton.frameNStart = frameN;  // exact frame index
      
      imageYesButton.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton.setAutoDraw(false);
    }
    
    // *imageNoButton* updates
    if (t >= 0.0 && imageNoButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton.tStart = t;  // (not accounting for frame time here)
      imageNoButton.frameNStart = frameN;  // exact frame index
      
      imageNoButton.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton.setAutoDraw(false);
    }
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse.status = PsychoJS.Status.FINISHED;
        }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof1' ---
    Prof1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof1.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof2Components;
function Prof2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof2' ---
    t = 0;
    Prof2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof2.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof2Components = [];
    Prof2Components.push(HaveYouTakenThisProf_2);
    Prof2Components.push(imageProf2);
    Prof2Components.push(imageYesButton_2);
    Prof2Components.push(imageNoButton_2);
    Prof2Components.push(mouse_2);
    
    Prof2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof2' ---
    // get current time
    t = Prof2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_2* updates
    if (t >= 0.0 && HaveYouTakenThisProf_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_2.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_2.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_2.setAutoDraw(false);
    }
    
    // *imageProf2* updates
    if (t >= 0.0 && imageProf2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf2.tStart = t;  // (not accounting for frame time here)
      imageProf2.frameNStart = frameN;  // exact frame index
      
      imageProf2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf2.setAutoDraw(false);
    }
    
    // *imageYesButton_2* updates
    if (t >= 0.0 && imageYesButton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_2.tStart = t;  // (not accounting for frame time here)
      imageYesButton_2.frameNStart = frameN;  // exact frame index
      
      imageYesButton_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_2.setAutoDraw(false);
    }
    
    // *imageNoButton_2* updates
    if (t >= 0.0 && imageNoButton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_2.tStart = t;  // (not accounting for frame time here)
      imageNoButton_2.frameNStart = frameN;  // exact frame index
      
      imageNoButton_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_2.setAutoDraw(false);
    }
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_2.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_2.getPos();
          mouse_2.x.push(_mouseXYs[0]);
          mouse_2.y.push(_mouseXYs[1]);
          mouse_2.leftButton.push(_mouseButtons[0]);
          mouse_2.midButton.push(_mouseButtons[1]);
          mouse_2.rightButton.push(_mouseButtons[2]);
          mouse_2.time.push(mouse_2.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof2' ---
    Prof2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof2.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_2.x) {  psychoJS.experiment.addData('mouse_2.x', mouse_2.x[0])};
    if (mouse_2.y) {  psychoJS.experiment.addData('mouse_2.y', mouse_2.y[0])};
    if (mouse_2.leftButton) {  psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton[0])};
    if (mouse_2.midButton) {  psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton[0])};
    if (mouse_2.rightButton) {  psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton[0])};
    if (mouse_2.time) {  psychoJS.experiment.addData('mouse_2.time', mouse_2.time[0])};
    if (mouse_2.clicked_name) {  psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof3Components;
function Prof3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof3' ---
    t = 0;
    Prof3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof3.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_3
    // current position of the mouse:
    mouse_3.x = [];
    mouse_3.y = [];
    mouse_3.leftButton = [];
    mouse_3.midButton = [];
    mouse_3.rightButton = [];
    mouse_3.time = [];
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof3Components = [];
    Prof3Components.push(HaveYouTakenThisProf_3);
    Prof3Components.push(imageProf3);
    Prof3Components.push(imageYesButton_3);
    Prof3Components.push(imageNoButton_3);
    Prof3Components.push(mouse_3);
    
    Prof3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof3' ---
    // get current time
    t = Prof3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_3* updates
    if (t >= 0.0 && HaveYouTakenThisProf_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_3.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_3.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_3.setAutoDraw(false);
    }
    
    // *imageProf3* updates
    if (t >= 0.0 && imageProf3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf3.tStart = t;  // (not accounting for frame time here)
      imageProf3.frameNStart = frameN;  // exact frame index
      
      imageProf3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf3.setAutoDraw(false);
    }
    
    // *imageYesButton_3* updates
    if (t >= 0.0 && imageYesButton_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_3.tStart = t;  // (not accounting for frame time here)
      imageYesButton_3.frameNStart = frameN;  // exact frame index
      
      imageYesButton_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_3.setAutoDraw(false);
    }
    
    // *imageNoButton_3* updates
    if (t >= 0.0 && imageNoButton_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_3.tStart = t;  // (not accounting for frame time here)
      imageNoButton_3.frameNStart = frameN;  // exact frame index
      
      imageNoButton_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_3.setAutoDraw(false);
    }
    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_3.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_3.getPos();
          mouse_3.x.push(_mouseXYs[0]);
          mouse_3.y.push(_mouseXYs[1]);
          mouse_3.leftButton.push(_mouseButtons[0]);
          mouse_3.midButton.push(_mouseButtons[1]);
          mouse_3.rightButton.push(_mouseButtons[2]);
          mouse_3.time.push(mouse_3.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof3' ---
    Prof3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof3.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_3.x) {  psychoJS.experiment.addData('mouse_3.x', mouse_3.x[0])};
    if (mouse_3.y) {  psychoJS.experiment.addData('mouse_3.y', mouse_3.y[0])};
    if (mouse_3.leftButton) {  psychoJS.experiment.addData('mouse_3.leftButton', mouse_3.leftButton[0])};
    if (mouse_3.midButton) {  psychoJS.experiment.addData('mouse_3.midButton', mouse_3.midButton[0])};
    if (mouse_3.rightButton) {  psychoJS.experiment.addData('mouse_3.rightButton', mouse_3.rightButton[0])};
    if (mouse_3.time) {  psychoJS.experiment.addData('mouse_3.time', mouse_3.time[0])};
    if (mouse_3.clicked_name) {  psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof4Components;
function Prof4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof4' ---
    t = 0;
    Prof4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof4.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_4
    // current position of the mouse:
    mouse_4.x = [];
    mouse_4.y = [];
    mouse_4.leftButton = [];
    mouse_4.midButton = [];
    mouse_4.rightButton = [];
    mouse_4.time = [];
    mouse_4.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof4Components = [];
    Prof4Components.push(HaveYouTakenThisProf_4);
    Prof4Components.push(imageProf4);
    Prof4Components.push(imageYesButton_4);
    Prof4Components.push(imageNoButton_4);
    Prof4Components.push(mouse_4);
    
    Prof4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof4' ---
    // get current time
    t = Prof4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_4* updates
    if (t >= 0.0 && HaveYouTakenThisProf_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_4.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_4.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_4.setAutoDraw(false);
    }
    
    // *imageProf4* updates
    if (t >= 0.0 && imageProf4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf4.tStart = t;  // (not accounting for frame time here)
      imageProf4.frameNStart = frameN;  // exact frame index
      
      imageProf4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf4.setAutoDraw(false);
    }
    
    // *imageYesButton_4* updates
    if (t >= 0.0 && imageYesButton_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_4.tStart = t;  // (not accounting for frame time here)
      imageYesButton_4.frameNStart = frameN;  // exact frame index
      
      imageYesButton_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_4.setAutoDraw(false);
    }
    
    // *imageNoButton_4* updates
    if (t >= 0.0 && imageNoButton_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_4.tStart = t;  // (not accounting for frame time here)
      imageNoButton_4.frameNStart = frameN;  // exact frame index
      
      imageNoButton_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_4.setAutoDraw(false);
    }
    // *mouse_4* updates
    if (t >= 0.0 && mouse_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_4.tStart = t;  // (not accounting for frame time here)
      mouse_4.frameNStart = frameN;  // exact frame index
      
      mouse_4.status = PsychoJS.Status.STARTED;
      mouse_4.mouseClock.reset();
      prevButtonState = mouse_4.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_4.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_4)) {
              gotValidClick = true;
              mouse_4.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_4.getPos();
          mouse_4.x.push(_mouseXYs[0]);
          mouse_4.y.push(_mouseXYs[1]);
          mouse_4.leftButton.push(_mouseButtons[0]);
          mouse_4.midButton.push(_mouseButtons[1]);
          mouse_4.rightButton.push(_mouseButtons[2]);
          mouse_4.time.push(mouse_4.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof4' ---
    Prof4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof4.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_4.x) {  psychoJS.experiment.addData('mouse_4.x', mouse_4.x[0])};
    if (mouse_4.y) {  psychoJS.experiment.addData('mouse_4.y', mouse_4.y[0])};
    if (mouse_4.leftButton) {  psychoJS.experiment.addData('mouse_4.leftButton', mouse_4.leftButton[0])};
    if (mouse_4.midButton) {  psychoJS.experiment.addData('mouse_4.midButton', mouse_4.midButton[0])};
    if (mouse_4.rightButton) {  psychoJS.experiment.addData('mouse_4.rightButton', mouse_4.rightButton[0])};
    if (mouse_4.time) {  psychoJS.experiment.addData('mouse_4.time', mouse_4.time[0])};
    if (mouse_4.clicked_name) {  psychoJS.experiment.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof5Components;
function Prof5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof5' ---
    t = 0;
    Prof5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof5.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_5
    // current position of the mouse:
    mouse_5.x = [];
    mouse_5.y = [];
    mouse_5.leftButton = [];
    mouse_5.midButton = [];
    mouse_5.rightButton = [];
    mouse_5.time = [];
    mouse_5.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof5Components = [];
    Prof5Components.push(HaveYouTakenThisProf_5);
    Prof5Components.push(imageProf5);
    Prof5Components.push(imageYesButton_5);
    Prof5Components.push(imageNoButton_5);
    Prof5Components.push(mouse_5);
    
    Prof5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof5' ---
    // get current time
    t = Prof5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_5* updates
    if (t >= 0.0 && HaveYouTakenThisProf_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_5.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_5.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_5.setAutoDraw(false);
    }
    
    // *imageProf5* updates
    if (t >= 0.0 && imageProf5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf5.tStart = t;  // (not accounting for frame time here)
      imageProf5.frameNStart = frameN;  // exact frame index
      
      imageProf5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf5.setAutoDraw(false);
    }
    
    // *imageYesButton_5* updates
    if (t >= 0.0 && imageYesButton_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_5.tStart = t;  // (not accounting for frame time here)
      imageYesButton_5.frameNStart = frameN;  // exact frame index
      
      imageYesButton_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_5.setAutoDraw(false);
    }
    
    // *imageNoButton_5* updates
    if (t >= 0.0 && imageNoButton_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_5.tStart = t;  // (not accounting for frame time here)
      imageNoButton_5.frameNStart = frameN;  // exact frame index
      
      imageNoButton_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_5.setAutoDraw(false);
    }
    // *mouse_5* updates
    if (t >= 0.0 && mouse_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_5.tStart = t;  // (not accounting for frame time here)
      mouse_5.frameNStart = frameN;  // exact frame index
      
      mouse_5.status = PsychoJS.Status.STARTED;
      mouse_5.mouseClock.reset();
      prevButtonState = mouse_5.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_5.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_5.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_5.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_5)) {
              gotValidClick = true;
              mouse_5.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_5.getPos();
          mouse_5.x.push(_mouseXYs[0]);
          mouse_5.y.push(_mouseXYs[1]);
          mouse_5.leftButton.push(_mouseButtons[0]);
          mouse_5.midButton.push(_mouseButtons[1]);
          mouse_5.rightButton.push(_mouseButtons[2]);
          mouse_5.time.push(mouse_5.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof5' ---
    Prof5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof5.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_5.x) {  psychoJS.experiment.addData('mouse_5.x', mouse_5.x[0])};
    if (mouse_5.y) {  psychoJS.experiment.addData('mouse_5.y', mouse_5.y[0])};
    if (mouse_5.leftButton) {  psychoJS.experiment.addData('mouse_5.leftButton', mouse_5.leftButton[0])};
    if (mouse_5.midButton) {  psychoJS.experiment.addData('mouse_5.midButton', mouse_5.midButton[0])};
    if (mouse_5.rightButton) {  psychoJS.experiment.addData('mouse_5.rightButton', mouse_5.rightButton[0])};
    if (mouse_5.time) {  psychoJS.experiment.addData('mouse_5.time', mouse_5.time[0])};
    if (mouse_5.clicked_name) {  psychoJS.experiment.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof6Components;
function Prof6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof6' ---
    t = 0;
    Prof6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof6.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_6
    // current position of the mouse:
    mouse_6.x = [];
    mouse_6.y = [];
    mouse_6.leftButton = [];
    mouse_6.midButton = [];
    mouse_6.rightButton = [];
    mouse_6.time = [];
    mouse_6.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof6Components = [];
    Prof6Components.push(HaveYouTakenThisProf_6);
    Prof6Components.push(imageProf6);
    Prof6Components.push(imageYesButton_6);
    Prof6Components.push(imageNoButton_6);
    Prof6Components.push(mouse_6);
    
    Prof6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof6' ---
    // get current time
    t = Prof6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_6* updates
    if (t >= 0.0 && HaveYouTakenThisProf_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_6.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_6.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_6.setAutoDraw(false);
    }
    
    // *imageProf6* updates
    if (t >= 0.0 && imageProf6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf6.tStart = t;  // (not accounting for frame time here)
      imageProf6.frameNStart = frameN;  // exact frame index
      
      imageProf6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf6.setAutoDraw(false);
    }
    
    // *imageYesButton_6* updates
    if (t >= 0.0 && imageYesButton_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_6.tStart = t;  // (not accounting for frame time here)
      imageYesButton_6.frameNStart = frameN;  // exact frame index
      
      imageYesButton_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_6.setAutoDraw(false);
    }
    
    // *imageNoButton_6* updates
    if (t >= 0.0 && imageNoButton_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_6.tStart = t;  // (not accounting for frame time here)
      imageNoButton_6.frameNStart = frameN;  // exact frame index
      
      imageNoButton_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_6.setAutoDraw(false);
    }
    // *mouse_6* updates
    if (t >= 0.0 && mouse_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_6.tStart = t;  // (not accounting for frame time here)
      mouse_6.frameNStart = frameN;  // exact frame index
      
      mouse_6.status = PsychoJS.Status.STARTED;
      mouse_6.mouseClock.reset();
      prevButtonState = mouse_6.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_6.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_6.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_6.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_6)) {
              gotValidClick = true;
              mouse_6.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_6.getPos();
          mouse_6.x.push(_mouseXYs[0]);
          mouse_6.y.push(_mouseXYs[1]);
          mouse_6.leftButton.push(_mouseButtons[0]);
          mouse_6.midButton.push(_mouseButtons[1]);
          mouse_6.rightButton.push(_mouseButtons[2]);
          mouse_6.time.push(mouse_6.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof6' ---
    Prof6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof6.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_6.x) {  psychoJS.experiment.addData('mouse_6.x', mouse_6.x[0])};
    if (mouse_6.y) {  psychoJS.experiment.addData('mouse_6.y', mouse_6.y[0])};
    if (mouse_6.leftButton) {  psychoJS.experiment.addData('mouse_6.leftButton', mouse_6.leftButton[0])};
    if (mouse_6.midButton) {  psychoJS.experiment.addData('mouse_6.midButton', mouse_6.midButton[0])};
    if (mouse_6.rightButton) {  psychoJS.experiment.addData('mouse_6.rightButton', mouse_6.rightButton[0])};
    if (mouse_6.time) {  psychoJS.experiment.addData('mouse_6.time', mouse_6.time[0])};
    if (mouse_6.clicked_name) {  psychoJS.experiment.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof7Components;
function Prof7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof7' ---
    t = 0;
    Prof7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof7.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_7
    // current position of the mouse:
    mouse_7.x = [];
    mouse_7.y = [];
    mouse_7.leftButton = [];
    mouse_7.midButton = [];
    mouse_7.rightButton = [];
    mouse_7.time = [];
    mouse_7.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof7Components = [];
    Prof7Components.push(HaveYouTakenThisProf_7);
    Prof7Components.push(imageProf7);
    Prof7Components.push(imageYesButton_7);
    Prof7Components.push(imageNoButton_7);
    Prof7Components.push(mouse_7);
    
    Prof7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof7' ---
    // get current time
    t = Prof7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_7* updates
    if (t >= 0.0 && HaveYouTakenThisProf_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_7.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_7.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_7.setAutoDraw(false);
    }
    
    // *imageProf7* updates
    if (t >= 0.0 && imageProf7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf7.tStart = t;  // (not accounting for frame time here)
      imageProf7.frameNStart = frameN;  // exact frame index
      
      imageProf7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf7.setAutoDraw(false);
    }
    
    // *imageYesButton_7* updates
    if (t >= 0.0 && imageYesButton_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_7.tStart = t;  // (not accounting for frame time here)
      imageYesButton_7.frameNStart = frameN;  // exact frame index
      
      imageYesButton_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_7.setAutoDraw(false);
    }
    
    // *imageNoButton_7* updates
    if (t >= 0.0 && imageNoButton_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_7.tStart = t;  // (not accounting for frame time here)
      imageNoButton_7.frameNStart = frameN;  // exact frame index
      
      imageNoButton_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_7.setAutoDraw(false);
    }
    // *mouse_7* updates
    if (t >= 0.0 && mouse_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_7.tStart = t;  // (not accounting for frame time here)
      mouse_7.frameNStart = frameN;  // exact frame index
      
      mouse_7.status = PsychoJS.Status.STARTED;
      mouse_7.mouseClock.reset();
      prevButtonState = mouse_7.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_7.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_7.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_7.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_7)) {
              gotValidClick = true;
              mouse_7.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_7.getPos();
          mouse_7.x.push(_mouseXYs[0]);
          mouse_7.y.push(_mouseXYs[1]);
          mouse_7.leftButton.push(_mouseButtons[0]);
          mouse_7.midButton.push(_mouseButtons[1]);
          mouse_7.rightButton.push(_mouseButtons[2]);
          mouse_7.time.push(mouse_7.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof7' ---
    Prof7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof7.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_7.x) {  psychoJS.experiment.addData('mouse_7.x', mouse_7.x[0])};
    if (mouse_7.y) {  psychoJS.experiment.addData('mouse_7.y', mouse_7.y[0])};
    if (mouse_7.leftButton) {  psychoJS.experiment.addData('mouse_7.leftButton', mouse_7.leftButton[0])};
    if (mouse_7.midButton) {  psychoJS.experiment.addData('mouse_7.midButton', mouse_7.midButton[0])};
    if (mouse_7.rightButton) {  psychoJS.experiment.addData('mouse_7.rightButton', mouse_7.rightButton[0])};
    if (mouse_7.time) {  psychoJS.experiment.addData('mouse_7.time', mouse_7.time[0])};
    if (mouse_7.clicked_name) {  psychoJS.experiment.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof8Components;
function Prof8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof8' ---
    t = 0;
    Prof8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof8.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_8
    // current position of the mouse:
    mouse_8.x = [];
    mouse_8.y = [];
    mouse_8.leftButton = [];
    mouse_8.midButton = [];
    mouse_8.rightButton = [];
    mouse_8.time = [];
    mouse_8.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof8Components = [];
    Prof8Components.push(HaveYouTakenThisProf_8);
    Prof8Components.push(imageProf8);
    Prof8Components.push(imageYesButton_8);
    Prof8Components.push(imageNoButton_8);
    Prof8Components.push(mouse_8);
    
    Prof8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof8' ---
    // get current time
    t = Prof8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_8* updates
    if (t >= 0.0 && HaveYouTakenThisProf_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_8.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_8.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_8.setAutoDraw(false);
    }
    
    // *imageProf8* updates
    if (t >= 0.0 && imageProf8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf8.tStart = t;  // (not accounting for frame time here)
      imageProf8.frameNStart = frameN;  // exact frame index
      
      imageProf8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf8.setAutoDraw(false);
    }
    
    // *imageYesButton_8* updates
    if (t >= 0.0 && imageYesButton_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_8.tStart = t;  // (not accounting for frame time here)
      imageYesButton_8.frameNStart = frameN;  // exact frame index
      
      imageYesButton_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_8.setAutoDraw(false);
    }
    
    // *imageNoButton_8* updates
    if (t >= 0.0 && imageNoButton_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_8.tStart = t;  // (not accounting for frame time here)
      imageNoButton_8.frameNStart = frameN;  // exact frame index
      
      imageNoButton_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_8.setAutoDraw(false);
    }
    // *mouse_8* updates
    if (t >= 0.0 && mouse_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_8.tStart = t;  // (not accounting for frame time here)
      mouse_8.frameNStart = frameN;  // exact frame index
      
      mouse_8.status = PsychoJS.Status.STARTED;
      mouse_8.mouseClock.reset();
      prevButtonState = mouse_8.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_8.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_8.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_8.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_8)) {
              gotValidClick = true;
              mouse_8.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_8.getPos();
          mouse_8.x.push(_mouseXYs[0]);
          mouse_8.y.push(_mouseXYs[1]);
          mouse_8.leftButton.push(_mouseButtons[0]);
          mouse_8.midButton.push(_mouseButtons[1]);
          mouse_8.rightButton.push(_mouseButtons[2]);
          mouse_8.time.push(mouse_8.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof8' ---
    Prof8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof8.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_8.x) {  psychoJS.experiment.addData('mouse_8.x', mouse_8.x[0])};
    if (mouse_8.y) {  psychoJS.experiment.addData('mouse_8.y', mouse_8.y[0])};
    if (mouse_8.leftButton) {  psychoJS.experiment.addData('mouse_8.leftButton', mouse_8.leftButton[0])};
    if (mouse_8.midButton) {  psychoJS.experiment.addData('mouse_8.midButton', mouse_8.midButton[0])};
    if (mouse_8.rightButton) {  psychoJS.experiment.addData('mouse_8.rightButton', mouse_8.rightButton[0])};
    if (mouse_8.time) {  psychoJS.experiment.addData('mouse_8.time', mouse_8.time[0])};
    if (mouse_8.clicked_name) {  psychoJS.experiment.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof9Components;
function Prof9RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof9' ---
    t = 0;
    Prof9Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof9.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_9
    // current position of the mouse:
    mouse_9.x = [];
    mouse_9.y = [];
    mouse_9.leftButton = [];
    mouse_9.midButton = [];
    mouse_9.rightButton = [];
    mouse_9.time = [];
    mouse_9.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof9Components = [];
    Prof9Components.push(HaveYouTakenThisProf_9);
    Prof9Components.push(imageProf9);
    Prof9Components.push(imageYesButton_9);
    Prof9Components.push(imageNoButton_9);
    Prof9Components.push(mouse_9);
    
    Prof9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof9RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof9' ---
    // get current time
    t = Prof9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_9* updates
    if (t >= 0.0 && HaveYouTakenThisProf_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_9.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_9.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_9.setAutoDraw(false);
    }
    
    // *imageProf9* updates
    if (t >= 0.0 && imageProf9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf9.tStart = t;  // (not accounting for frame time here)
      imageProf9.frameNStart = frameN;  // exact frame index
      
      imageProf9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf9.setAutoDraw(false);
    }
    
    // *imageYesButton_9* updates
    if (t >= 0.0 && imageYesButton_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_9.tStart = t;  // (not accounting for frame time here)
      imageYesButton_9.frameNStart = frameN;  // exact frame index
      
      imageYesButton_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_9.setAutoDraw(false);
    }
    
    // *imageNoButton_9* updates
    if (t >= 0.0 && imageNoButton_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_9.tStart = t;  // (not accounting for frame time here)
      imageNoButton_9.frameNStart = frameN;  // exact frame index
      
      imageNoButton_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_9.setAutoDraw(false);
    }
    // *mouse_9* updates
    if (t >= 0.0 && mouse_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_9.tStart = t;  // (not accounting for frame time here)
      mouse_9.frameNStart = frameN;  // exact frame index
      
      mouse_9.status = PsychoJS.Status.STARTED;
      mouse_9.mouseClock.reset();
      prevButtonState = mouse_9.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_9.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_9.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_9.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_9)) {
              gotValidClick = true;
              mouse_9.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_9.getPos();
          mouse_9.x.push(_mouseXYs[0]);
          mouse_9.y.push(_mouseXYs[1]);
          mouse_9.leftButton.push(_mouseButtons[0]);
          mouse_9.midButton.push(_mouseButtons[1]);
          mouse_9.rightButton.push(_mouseButtons[2]);
          mouse_9.time.push(mouse_9.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof9RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof9' ---
    Prof9Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof9.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_9.x) {  psychoJS.experiment.addData('mouse_9.x', mouse_9.x[0])};
    if (mouse_9.y) {  psychoJS.experiment.addData('mouse_9.y', mouse_9.y[0])};
    if (mouse_9.leftButton) {  psychoJS.experiment.addData('mouse_9.leftButton', mouse_9.leftButton[0])};
    if (mouse_9.midButton) {  psychoJS.experiment.addData('mouse_9.midButton', mouse_9.midButton[0])};
    if (mouse_9.rightButton) {  psychoJS.experiment.addData('mouse_9.rightButton', mouse_9.rightButton[0])};
    if (mouse_9.time) {  psychoJS.experiment.addData('mouse_9.time', mouse_9.time[0])};
    if (mouse_9.clicked_name) {  psychoJS.experiment.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof10Components;
function Prof10RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof10' ---
    t = 0;
    Prof10Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof10.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_10
    // current position of the mouse:
    mouse_10.x = [];
    mouse_10.y = [];
    mouse_10.leftButton = [];
    mouse_10.midButton = [];
    mouse_10.rightButton = [];
    mouse_10.time = [];
    mouse_10.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof10Components = [];
    Prof10Components.push(HaveYouTakenThisProf_10);
    Prof10Components.push(imageProf10);
    Prof10Components.push(imageYesButton_10);
    Prof10Components.push(imageNoButton_10);
    Prof10Components.push(mouse_10);
    
    Prof10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof10RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof10' ---
    // get current time
    t = Prof10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_10* updates
    if (t >= 0.0 && HaveYouTakenThisProf_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_10.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_10.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_10.setAutoDraw(false);
    }
    
    // *imageProf10* updates
    if (t >= 0.0 && imageProf10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf10.tStart = t;  // (not accounting for frame time here)
      imageProf10.frameNStart = frameN;  // exact frame index
      
      imageProf10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf10.setAutoDraw(false);
    }
    
    // *imageYesButton_10* updates
    if (t >= 0.0 && imageYesButton_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_10.tStart = t;  // (not accounting for frame time here)
      imageYesButton_10.frameNStart = frameN;  // exact frame index
      
      imageYesButton_10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_10.setAutoDraw(false);
    }
    
    // *imageNoButton_10* updates
    if (t >= 0.0 && imageNoButton_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_10.tStart = t;  // (not accounting for frame time here)
      imageNoButton_10.frameNStart = frameN;  // exact frame index
      
      imageNoButton_10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_10.setAutoDraw(false);
    }
    // *mouse_10* updates
    if (t >= 0.0 && mouse_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_10.tStart = t;  // (not accounting for frame time here)
      mouse_10.frameNStart = frameN;  // exact frame index
      
      mouse_10.status = PsychoJS.Status.STARTED;
      mouse_10.mouseClock.reset();
      prevButtonState = mouse_10.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_10.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_10.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_10.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_10)) {
              gotValidClick = true;
              mouse_10.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_10.getPos();
          mouse_10.x.push(_mouseXYs[0]);
          mouse_10.y.push(_mouseXYs[1]);
          mouse_10.leftButton.push(_mouseButtons[0]);
          mouse_10.midButton.push(_mouseButtons[1]);
          mouse_10.rightButton.push(_mouseButtons[2]);
          mouse_10.time.push(mouse_10.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof10RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof10' ---
    Prof10Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof10.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_10.x) {  psychoJS.experiment.addData('mouse_10.x', mouse_10.x[0])};
    if (mouse_10.y) {  psychoJS.experiment.addData('mouse_10.y', mouse_10.y[0])};
    if (mouse_10.leftButton) {  psychoJS.experiment.addData('mouse_10.leftButton', mouse_10.leftButton[0])};
    if (mouse_10.midButton) {  psychoJS.experiment.addData('mouse_10.midButton', mouse_10.midButton[0])};
    if (mouse_10.rightButton) {  psychoJS.experiment.addData('mouse_10.rightButton', mouse_10.rightButton[0])};
    if (mouse_10.time) {  psychoJS.experiment.addData('mouse_10.time', mouse_10.time[0])};
    if (mouse_10.clicked_name) {  psychoJS.experiment.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof11Components;
function Prof11RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof11' ---
    t = 0;
    Prof11Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof11.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_11
    // current position of the mouse:
    mouse_11.x = [];
    mouse_11.y = [];
    mouse_11.leftButton = [];
    mouse_11.midButton = [];
    mouse_11.rightButton = [];
    mouse_11.time = [];
    mouse_11.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof11Components = [];
    Prof11Components.push(HaveYouTakenThisProf_11);
    Prof11Components.push(imageProf11);
    Prof11Components.push(imageYesButton_11);
    Prof11Components.push(imageNoButton_11);
    Prof11Components.push(mouse_11);
    
    Prof11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof11RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof11' ---
    // get current time
    t = Prof11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_11* updates
    if (t >= 0.0 && HaveYouTakenThisProf_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_11.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_11.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_11.setAutoDraw(false);
    }
    
    // *imageProf11* updates
    if (t >= 0.0 && imageProf11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf11.tStart = t;  // (not accounting for frame time here)
      imageProf11.frameNStart = frameN;  // exact frame index
      
      imageProf11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf11.setAutoDraw(false);
    }
    
    // *imageYesButton_11* updates
    if (t >= 0.0 && imageYesButton_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_11.tStart = t;  // (not accounting for frame time here)
      imageYesButton_11.frameNStart = frameN;  // exact frame index
      
      imageYesButton_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_11.setAutoDraw(false);
    }
    
    // *imageNoButton_11* updates
    if (t >= 0.0 && imageNoButton_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_11.tStart = t;  // (not accounting for frame time here)
      imageNoButton_11.frameNStart = frameN;  // exact frame index
      
      imageNoButton_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_11.setAutoDraw(false);
    }
    // *mouse_11* updates
    if (t >= 0.0 && mouse_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_11.tStart = t;  // (not accounting for frame time here)
      mouse_11.frameNStart = frameN;  // exact frame index
      
      mouse_11.status = PsychoJS.Status.STARTED;
      mouse_11.mouseClock.reset();
      prevButtonState = mouse_11.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_11.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_11.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_11.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_11)) {
              gotValidClick = true;
              mouse_11.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_11.getPos();
          mouse_11.x.push(_mouseXYs[0]);
          mouse_11.y.push(_mouseXYs[1]);
          mouse_11.leftButton.push(_mouseButtons[0]);
          mouse_11.midButton.push(_mouseButtons[1]);
          mouse_11.rightButton.push(_mouseButtons[2]);
          mouse_11.time.push(mouse_11.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof11RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof11' ---
    Prof11Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof11.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_11.x) {  psychoJS.experiment.addData('mouse_11.x', mouse_11.x[0])};
    if (mouse_11.y) {  psychoJS.experiment.addData('mouse_11.y', mouse_11.y[0])};
    if (mouse_11.leftButton) {  psychoJS.experiment.addData('mouse_11.leftButton', mouse_11.leftButton[0])};
    if (mouse_11.midButton) {  psychoJS.experiment.addData('mouse_11.midButton', mouse_11.midButton[0])};
    if (mouse_11.rightButton) {  psychoJS.experiment.addData('mouse_11.rightButton', mouse_11.rightButton[0])};
    if (mouse_11.time) {  psychoJS.experiment.addData('mouse_11.time', mouse_11.time[0])};
    if (mouse_11.clicked_name) {  psychoJS.experiment.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof12Components;
function Prof12RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof12' ---
    t = 0;
    Prof12Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof12.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_12
    // current position of the mouse:
    mouse_12.x = [];
    mouse_12.y = [];
    mouse_12.leftButton = [];
    mouse_12.midButton = [];
    mouse_12.rightButton = [];
    mouse_12.time = [];
    mouse_12.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof12Components = [];
    Prof12Components.push(HaveYouTakenThisProf_12);
    Prof12Components.push(imageProf12);
    Prof12Components.push(imageYesButton_12);
    Prof12Components.push(imageNoButton_12);
    Prof12Components.push(mouse_12);
    
    Prof12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof12RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof12' ---
    // get current time
    t = Prof12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_12* updates
    if (t >= 0.0 && HaveYouTakenThisProf_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_12.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_12.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_12.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_12.setAutoDraw(false);
    }
    
    // *imageProf12* updates
    if (t >= 0.0 && imageProf12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf12.tStart = t;  // (not accounting for frame time here)
      imageProf12.frameNStart = frameN;  // exact frame index
      
      imageProf12.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf12.setAutoDraw(false);
    }
    
    // *imageYesButton_12* updates
    if (t >= 0.0 && imageYesButton_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_12.tStart = t;  // (not accounting for frame time here)
      imageYesButton_12.frameNStart = frameN;  // exact frame index
      
      imageYesButton_12.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_12.setAutoDraw(false);
    }
    
    // *imageNoButton_12* updates
    if (t >= 0.0 && imageNoButton_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_12.tStart = t;  // (not accounting for frame time here)
      imageNoButton_12.frameNStart = frameN;  // exact frame index
      
      imageNoButton_12.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_12.setAutoDraw(false);
    }
    // *mouse_12* updates
    if (t >= 0.0 && mouse_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_12.tStart = t;  // (not accounting for frame time here)
      mouse_12.frameNStart = frameN;  // exact frame index
      
      mouse_12.status = PsychoJS.Status.STARTED;
      mouse_12.mouseClock.reset();
      prevButtonState = mouse_12.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_12.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_12.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_12.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_12)) {
              gotValidClick = true;
              mouse_12.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_12.getPos();
          mouse_12.x.push(_mouseXYs[0]);
          mouse_12.y.push(_mouseXYs[1]);
          mouse_12.leftButton.push(_mouseButtons[0]);
          mouse_12.midButton.push(_mouseButtons[1]);
          mouse_12.rightButton.push(_mouseButtons[2]);
          mouse_12.time.push(mouse_12.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof12RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof12' ---
    Prof12Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof12.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_12.x) {  psychoJS.experiment.addData('mouse_12.x', mouse_12.x[0])};
    if (mouse_12.y) {  psychoJS.experiment.addData('mouse_12.y', mouse_12.y[0])};
    if (mouse_12.leftButton) {  psychoJS.experiment.addData('mouse_12.leftButton', mouse_12.leftButton[0])};
    if (mouse_12.midButton) {  psychoJS.experiment.addData('mouse_12.midButton', mouse_12.midButton[0])};
    if (mouse_12.rightButton) {  psychoJS.experiment.addData('mouse_12.rightButton', mouse_12.rightButton[0])};
    if (mouse_12.time) {  psychoJS.experiment.addData('mouse_12.time', mouse_12.time[0])};
    if (mouse_12.clicked_name) {  psychoJS.experiment.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof13Components;
function Prof13RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof13' ---
    t = 0;
    Prof13Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof13.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_13
    // current position of the mouse:
    mouse_13.x = [];
    mouse_13.y = [];
    mouse_13.leftButton = [];
    mouse_13.midButton = [];
    mouse_13.rightButton = [];
    mouse_13.time = [];
    mouse_13.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof13Components = [];
    Prof13Components.push(HaveYouTakenThisProf_13);
    Prof13Components.push(imageProf13);
    Prof13Components.push(imageYesButton_13);
    Prof13Components.push(imageNoButton_13);
    Prof13Components.push(mouse_13);
    
    Prof13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof13RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof13' ---
    // get current time
    t = Prof13Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_13* updates
    if (t >= 0.0 && HaveYouTakenThisProf_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_13.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_13.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_13.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_13.setAutoDraw(false);
    }
    
    // *imageProf13* updates
    if (t >= 0.0 && imageProf13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf13.tStart = t;  // (not accounting for frame time here)
      imageProf13.frameNStart = frameN;  // exact frame index
      
      imageProf13.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf13.setAutoDraw(false);
    }
    
    // *imageYesButton_13* updates
    if (t >= 0.0 && imageYesButton_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_13.tStart = t;  // (not accounting for frame time here)
      imageYesButton_13.frameNStart = frameN;  // exact frame index
      
      imageYesButton_13.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_13.setAutoDraw(false);
    }
    
    // *imageNoButton_13* updates
    if (t >= 0.0 && imageNoButton_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_13.tStart = t;  // (not accounting for frame time here)
      imageNoButton_13.frameNStart = frameN;  // exact frame index
      
      imageNoButton_13.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_13.setAutoDraw(false);
    }
    // *mouse_13* updates
    if (t >= 0.0 && mouse_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_13.tStart = t;  // (not accounting for frame time here)
      mouse_13.frameNStart = frameN;  // exact frame index
      
      mouse_13.status = PsychoJS.Status.STARTED;
      mouse_13.mouseClock.reset();
      prevButtonState = mouse_13.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_13.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_13.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_13.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_13)) {
              gotValidClick = true;
              mouse_13.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_13.getPos();
          mouse_13.x.push(_mouseXYs[0]);
          mouse_13.y.push(_mouseXYs[1]);
          mouse_13.leftButton.push(_mouseButtons[0]);
          mouse_13.midButton.push(_mouseButtons[1]);
          mouse_13.rightButton.push(_mouseButtons[2]);
          mouse_13.time.push(mouse_13.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof13RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof13' ---
    Prof13Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof13.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_13.x) {  psychoJS.experiment.addData('mouse_13.x', mouse_13.x[0])};
    if (mouse_13.y) {  psychoJS.experiment.addData('mouse_13.y', mouse_13.y[0])};
    if (mouse_13.leftButton) {  psychoJS.experiment.addData('mouse_13.leftButton', mouse_13.leftButton[0])};
    if (mouse_13.midButton) {  psychoJS.experiment.addData('mouse_13.midButton', mouse_13.midButton[0])};
    if (mouse_13.rightButton) {  psychoJS.experiment.addData('mouse_13.rightButton', mouse_13.rightButton[0])};
    if (mouse_13.time) {  psychoJS.experiment.addData('mouse_13.time', mouse_13.time[0])};
    if (mouse_13.clicked_name) {  psychoJS.experiment.addData('mouse_13.clicked_name', mouse_13.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof14Components;
function Prof14RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof14' ---
    t = 0;
    Prof14Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof14.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_14
    // current position of the mouse:
    mouse_14.x = [];
    mouse_14.y = [];
    mouse_14.leftButton = [];
    mouse_14.midButton = [];
    mouse_14.rightButton = [];
    mouse_14.time = [];
    mouse_14.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof14Components = [];
    Prof14Components.push(HaveYouTakenThisProf_14);
    Prof14Components.push(imageProf14);
    Prof14Components.push(imageYesButton_14);
    Prof14Components.push(imageNoButton_14);
    Prof14Components.push(mouse_14);
    
    Prof14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof14RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof14' ---
    // get current time
    t = Prof14Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_14* updates
    if (t >= 0.0 && HaveYouTakenThisProf_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_14.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_14.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_14.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_14.setAutoDraw(false);
    }
    
    // *imageProf14* updates
    if (t >= 0.0 && imageProf14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf14.tStart = t;  // (not accounting for frame time here)
      imageProf14.frameNStart = frameN;  // exact frame index
      
      imageProf14.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf14.setAutoDraw(false);
    }
    
    // *imageYesButton_14* updates
    if (t >= 0.0 && imageYesButton_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_14.tStart = t;  // (not accounting for frame time here)
      imageYesButton_14.frameNStart = frameN;  // exact frame index
      
      imageYesButton_14.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_14.setAutoDraw(false);
    }
    
    // *imageNoButton_14* updates
    if (t >= 0.0 && imageNoButton_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_14.tStart = t;  // (not accounting for frame time here)
      imageNoButton_14.frameNStart = frameN;  // exact frame index
      
      imageNoButton_14.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_14.setAutoDraw(false);
    }
    // *mouse_14* updates
    if (t >= 0.0 && mouse_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_14.tStart = t;  // (not accounting for frame time here)
      mouse_14.frameNStart = frameN;  // exact frame index
      
      mouse_14.status = PsychoJS.Status.STARTED;
      mouse_14.mouseClock.reset();
      prevButtonState = mouse_14.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_14.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_14.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_14.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_14)) {
              gotValidClick = true;
              mouse_14.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_14.getPos();
          mouse_14.x.push(_mouseXYs[0]);
          mouse_14.y.push(_mouseXYs[1]);
          mouse_14.leftButton.push(_mouseButtons[0]);
          mouse_14.midButton.push(_mouseButtons[1]);
          mouse_14.rightButton.push(_mouseButtons[2]);
          mouse_14.time.push(mouse_14.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof14RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof14' ---
    Prof14Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof14.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_14.x) {  psychoJS.experiment.addData('mouse_14.x', mouse_14.x[0])};
    if (mouse_14.y) {  psychoJS.experiment.addData('mouse_14.y', mouse_14.y[0])};
    if (mouse_14.leftButton) {  psychoJS.experiment.addData('mouse_14.leftButton', mouse_14.leftButton[0])};
    if (mouse_14.midButton) {  psychoJS.experiment.addData('mouse_14.midButton', mouse_14.midButton[0])};
    if (mouse_14.rightButton) {  psychoJS.experiment.addData('mouse_14.rightButton', mouse_14.rightButton[0])};
    if (mouse_14.time) {  psychoJS.experiment.addData('mouse_14.time', mouse_14.time[0])};
    if (mouse_14.clicked_name) {  psychoJS.experiment.addData('mouse_14.clicked_name', mouse_14.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof15Components;
function Prof15RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof15' ---
    t = 0;
    Prof15Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof15.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_15
    // current position of the mouse:
    mouse_15.x = [];
    mouse_15.y = [];
    mouse_15.leftButton = [];
    mouse_15.midButton = [];
    mouse_15.rightButton = [];
    mouse_15.time = [];
    mouse_15.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof15Components = [];
    Prof15Components.push(HaveYouTakenThisProf_15);
    Prof15Components.push(imageProf15);
    Prof15Components.push(imageYesButton_15);
    Prof15Components.push(imageNoButton_15);
    Prof15Components.push(mouse_15);
    
    Prof15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof15RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof15' ---
    // get current time
    t = Prof15Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_15* updates
    if (t >= 0.0 && HaveYouTakenThisProf_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_15.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_15.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_15.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_15.setAutoDraw(false);
    }
    
    // *imageProf15* updates
    if (t >= 0.0 && imageProf15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf15.tStart = t;  // (not accounting for frame time here)
      imageProf15.frameNStart = frameN;  // exact frame index
      
      imageProf15.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf15.setAutoDraw(false);
    }
    
    // *imageYesButton_15* updates
    if (t >= 0.0 && imageYesButton_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_15.tStart = t;  // (not accounting for frame time here)
      imageYesButton_15.frameNStart = frameN;  // exact frame index
      
      imageYesButton_15.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_15.setAutoDraw(false);
    }
    
    // *imageNoButton_15* updates
    if (t >= 0.0 && imageNoButton_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_15.tStart = t;  // (not accounting for frame time here)
      imageNoButton_15.frameNStart = frameN;  // exact frame index
      
      imageNoButton_15.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_15.setAutoDraw(false);
    }
    // *mouse_15* updates
    if (t >= 0.0 && mouse_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_15.tStart = t;  // (not accounting for frame time here)
      mouse_15.frameNStart = frameN;  // exact frame index
      
      mouse_15.status = PsychoJS.Status.STARTED;
      mouse_15.mouseClock.reset();
      prevButtonState = mouse_15.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_15.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_15.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_15.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_15)) {
              gotValidClick = true;
              mouse_15.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_15.getPos();
          mouse_15.x.push(_mouseXYs[0]);
          mouse_15.y.push(_mouseXYs[1]);
          mouse_15.leftButton.push(_mouseButtons[0]);
          mouse_15.midButton.push(_mouseButtons[1]);
          mouse_15.rightButton.push(_mouseButtons[2]);
          mouse_15.time.push(mouse_15.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof15RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof15' ---
    Prof15Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof15.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_15.x) {  psychoJS.experiment.addData('mouse_15.x', mouse_15.x[0])};
    if (mouse_15.y) {  psychoJS.experiment.addData('mouse_15.y', mouse_15.y[0])};
    if (mouse_15.leftButton) {  psychoJS.experiment.addData('mouse_15.leftButton', mouse_15.leftButton[0])};
    if (mouse_15.midButton) {  psychoJS.experiment.addData('mouse_15.midButton', mouse_15.midButton[0])};
    if (mouse_15.rightButton) {  psychoJS.experiment.addData('mouse_15.rightButton', mouse_15.rightButton[0])};
    if (mouse_15.time) {  psychoJS.experiment.addData('mouse_15.time', mouse_15.time[0])};
    if (mouse_15.clicked_name) {  psychoJS.experiment.addData('mouse_15.clicked_name', mouse_15.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof16Components;
function Prof16RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof16' ---
    t = 0;
    Prof16Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof16.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_16
    // current position of the mouse:
    mouse_16.x = [];
    mouse_16.y = [];
    mouse_16.leftButton = [];
    mouse_16.midButton = [];
    mouse_16.rightButton = [];
    mouse_16.time = [];
    mouse_16.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof16Components = [];
    Prof16Components.push(HaveYouTakenThisProf_16);
    Prof16Components.push(imageProf16);
    Prof16Components.push(imageYesButton_16);
    Prof16Components.push(imageNoButton_16);
    Prof16Components.push(mouse_16);
    
    Prof16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof16RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof16' ---
    // get current time
    t = Prof16Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_16* updates
    if (t >= 0.0 && HaveYouTakenThisProf_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_16.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_16.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_16.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_16.setAutoDraw(false);
    }
    
    // *imageProf16* updates
    if (t >= 0.0 && imageProf16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf16.tStart = t;  // (not accounting for frame time here)
      imageProf16.frameNStart = frameN;  // exact frame index
      
      imageProf16.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf16.setAutoDraw(false);
    }
    
    // *imageYesButton_16* updates
    if (t >= 0.0 && imageYesButton_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_16.tStart = t;  // (not accounting for frame time here)
      imageYesButton_16.frameNStart = frameN;  // exact frame index
      
      imageYesButton_16.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_16.setAutoDraw(false);
    }
    
    // *imageNoButton_16* updates
    if (t >= 0.0 && imageNoButton_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_16.tStart = t;  // (not accounting for frame time here)
      imageNoButton_16.frameNStart = frameN;  // exact frame index
      
      imageNoButton_16.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_16.setAutoDraw(false);
    }
    // *mouse_16* updates
    if (t >= 0.0 && mouse_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_16.tStart = t;  // (not accounting for frame time here)
      mouse_16.frameNStart = frameN;  // exact frame index
      
      mouse_16.status = PsychoJS.Status.STARTED;
      mouse_16.mouseClock.reset();
      prevButtonState = mouse_16.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_16.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_16.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_16.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_16)) {
              gotValidClick = true;
              mouse_16.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_16.getPos();
          mouse_16.x.push(_mouseXYs[0]);
          mouse_16.y.push(_mouseXYs[1]);
          mouse_16.leftButton.push(_mouseButtons[0]);
          mouse_16.midButton.push(_mouseButtons[1]);
          mouse_16.rightButton.push(_mouseButtons[2]);
          mouse_16.time.push(mouse_16.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof16RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof16' ---
    Prof16Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof16.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_16.x) {  psychoJS.experiment.addData('mouse_16.x', mouse_16.x[0])};
    if (mouse_16.y) {  psychoJS.experiment.addData('mouse_16.y', mouse_16.y[0])};
    if (mouse_16.leftButton) {  psychoJS.experiment.addData('mouse_16.leftButton', mouse_16.leftButton[0])};
    if (mouse_16.midButton) {  psychoJS.experiment.addData('mouse_16.midButton', mouse_16.midButton[0])};
    if (mouse_16.rightButton) {  psychoJS.experiment.addData('mouse_16.rightButton', mouse_16.rightButton[0])};
    if (mouse_16.time) {  psychoJS.experiment.addData('mouse_16.time', mouse_16.time[0])};
    if (mouse_16.clicked_name) {  psychoJS.experiment.addData('mouse_16.clicked_name', mouse_16.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Prof17Components;
function Prof17RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prof17' ---
    t = 0;
    Prof17Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Prof17.started', globalClock.getTime());
    // setup some python lists for storing info about the mouse_17
    // current position of the mouse:
    mouse_17.x = [];
    mouse_17.y = [];
    mouse_17.leftButton = [];
    mouse_17.midButton = [];
    mouse_17.rightButton = [];
    mouse_17.time = [];
    mouse_17.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    Prof17Components = [];
    Prof17Components.push(HaveYouTakenThisProf_17);
    Prof17Components.push(imageProf17);
    Prof17Components.push(imageYesButton_17);
    Prof17Components.push(imageNoButton_17);
    Prof17Components.push(mouse_17);
    
    Prof17Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Prof17RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prof17' ---
    // get current time
    t = Prof17Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HaveYouTakenThisProf_17* updates
    if (t >= 0.0 && HaveYouTakenThisProf_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HaveYouTakenThisProf_17.tStart = t;  // (not accounting for frame time here)
      HaveYouTakenThisProf_17.frameNStart = frameN;  // exact frame index
      
      HaveYouTakenThisProf_17.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (HaveYouTakenThisProf_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      HaveYouTakenThisProf_17.setAutoDraw(false);
    }
    
    // *imageProf17* updates
    if (t >= 0.0 && imageProf17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageProf17.tStart = t;  // (not accounting for frame time here)
      imageProf17.frameNStart = frameN;  // exact frame index
      
      imageProf17.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageProf17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageProf17.setAutoDraw(false);
    }
    
    // *imageYesButton_17* updates
    if (t >= 0.0 && imageYesButton_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageYesButton_17.tStart = t;  // (not accounting for frame time here)
      imageYesButton_17.frameNStart = frameN;  // exact frame index
      
      imageYesButton_17.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageYesButton_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageYesButton_17.setAutoDraw(false);
    }
    
    // *imageNoButton_17* updates
    if (t >= 0.0 && imageNoButton_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imageNoButton_17.tStart = t;  // (not accounting for frame time here)
      imageNoButton_17.frameNStart = frameN;  // exact frame index
      
      imageNoButton_17.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imageNoButton_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imageNoButton_17.setAutoDraw(false);
    }
    // *mouse_17* updates
    if (t >= 0.0 && mouse_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_17.tStart = t;  // (not accounting for frame time here)
      mouse_17.frameNStart = frameN;  // exact frame index
      
      mouse_17.status = PsychoJS.Status.STARTED;
      mouse_17.mouseClock.reset();
      prevButtonState = mouse_17.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_17.status = PsychoJS.Status.FINISHED;
        }
    if (mouse_17.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_17.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of ['imageYesButton', 'imageNoButton']) {
            if (obj.contains(mouse_17)) {
              gotValidClick = true;
              mouse_17.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_17.getPos();
          mouse_17.x.push(_mouseXYs[0]);
          mouse_17.y.push(_mouseXYs[1]);
          mouse_17.leftButton.push(_mouseButtons[0]);
          mouse_17.midButton.push(_mouseButtons[1]);
          mouse_17.rightButton.push(_mouseButtons[2]);
          mouse_17.time.push(mouse_17.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Prof17Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prof17RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prof17' ---
    Prof17Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Prof17.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_17.x) {  psychoJS.experiment.addData('mouse_17.x', mouse_17.x[0])};
    if (mouse_17.y) {  psychoJS.experiment.addData('mouse_17.y', mouse_17.y[0])};
    if (mouse_17.leftButton) {  psychoJS.experiment.addData('mouse_17.leftButton', mouse_17.leftButton[0])};
    if (mouse_17.midButton) {  psychoJS.experiment.addData('mouse_17.midButton', mouse_17.midButton[0])};
    if (mouse_17.rightButton) {  psychoJS.experiment.addData('mouse_17.rightButton', mouse_17.rightButton[0])};
    if (mouse_17.time) {  psychoJS.experiment.addData('mouse_17.time', mouse_17.time[0])};
    if (mouse_17.clicked_name) {  psychoJS.experiment.addData('mouse_17.clicked_name', mouse_17.clicked_name[0])};
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ThankYouScreenComponents;
function ThankYouScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYouScreen' ---
    t = 0;
    ThankYouScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('ThankYouScreen.started', globalClock.getTime());
    // keep track of which components have finished
    ThankYouScreenComponents = [];
    ThankYouScreenComponents.push(textThankYouMessage);
    
    ThankYouScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ThankYouScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYouScreen' ---
    // get current time
    t = ThankYouScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textThankYouMessage* updates
    if (t >= 0.0 && textThankYouMessage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textThankYouMessage.tStart = t;  // (not accounting for frame time here)
      textThankYouMessage.frameNStart = frameN;  // exact frame index
      
      textThankYouMessage.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textThankYouMessage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textThankYouMessage.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ThankYouScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThankYouScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYouScreen' ---
    ThankYouScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ThankYouScreen.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
