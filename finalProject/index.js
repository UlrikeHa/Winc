'use strict';

const mockData = require('./mockData.js').data;

// define variables
const userProfile = {};

const profileQuestions = [
  "What is your first name?",
  "What is your last name?",
  "What is your age?",
  "What is your gender? (F, M, X)",
  "Which gender are you interested in? (F, M, B, X)",
  "What is your location? (city/rural)",
  "What minimum age are you interested in?",
  "What maximum age are you interested in?",
];

const profileInput = [];
const matchesFound = [];
let answerCounter = 0;
let matchCounter = 0;

// prompt questions using a while loop

console.log('Please answer following questions!\r\n');

while (answerCounter < profileQuestions.length) {
  const question = profileQuestions[answerCounter]
  const answer = prompt(question);
  const legaleAge = 18;
  const locations = ['rural', 'city'];
  const userGender = ['F', 'M', 'X']; // female, male, everything else
  const genderOptions = ['F', 'M', 'B', 'X']; //female, male, both, everything else

// check if name is not empty strings 
  
  if (answerCounter == 0 && answer.length < 1) {
    console.log('Please enter your first name!');
    continue;
  }
  
  if (answerCounter == 1 && answer.length < 1) {
    console.log('Please enter your last name!');
    continue;
  }
  
// check answer is a number
  
  if (answerCounter == 2 && isNaN(answer)) {
    console.log('Please enter a number!');
    continue;
  }

  if (answerCounter == 6 && isNaN(answer)) {
    console.log('Please enter a number!');
    continue;
  }

  if (answerCounter == 7 && isNaN(answer)) {
    console.log('Please enter a number!');
    continue;
  }
  
// check legale age
  
  if (answerCounter == 2 && answer < legaleAge) {
    console.log('You must be at least 18 years     old!');
    continue;
  }
  
  if (answerCounter == 6 && answer < legaleAge) {
    console.log('The minimum age must be 18 or higher!');
    continue;
  }

//check maximum age is higher than minimum age
  
if (answerCounter == 7 && answer < profileInput[6]) {
    console.log('The maximum age must be higher than minimum age!');
    continue;
  }
  
// check if answer is chosen from given options
  
if (answerCounter == 3 && !userGender.includes(answer)) {
  console.log('Please choose from (F, M, X)!');
  continue;
}

if (answerCounter == 4 && !genderOptions.includes(answer)) {
  console.log('Please choose from (F, M, B, X)!');
  continue;
}

if (answerCounter == 5 && !locations.includes(answer)) {
  console.log('Please choose city or rural!');
  continue;
}
  
// store answers in profileInput
  
  profileInput.push(answer);
  answerCounter ++;
}

// store user input in userProfile

userProfile.first_name = profileInput[0];
userProfile.last_name = profileInput[1];
userProfile.age = profileInput[2];
userProfile.gender = profileInput[3];
userProfile.gender_interest = profileInput[4];
userProfile.location = profileInput[5];
userProfile.min_age_interest = profileInput[6];
userProfile.max_age_interest = profileInput[7];

// compare userProfile with mockData

for (let i = 0; i < mockData.length; i++) {
  if (userProfile.age >= mockData[i].min_age_interest && userProfile.age <= mockData[i].max_age_interest) {
    if (mockData[i].age >= userProfile.min_age_interest && mockData[i].age <= userProfile.max_age_interest){
      if (mockData[i].location == userProfile.location) {
        if ((userProfile.gender_interest == mockData[i].gender) || (userProfile.gender_interest == "B") && (["M", "F"].includes(mockData[i].gender))) {
          if ((mockData[i].gender_interest == userProfile.gender) || (mockData[i].gender_interest == "B") && (["M", "F"].includes(userProfile.gender))) { 
            
            // store matches in matchesFound
            matchesFound.push(mockData[i]);
            matchCounter++; }
         } 
      }
    }  
  }
}

console.log("-------------------------------------");
// print results

if (matchCounter == 0) { // no match found
  console.log(`Sorry ${userProfile.first_name}, we didn't find a match for you. Think about your dating interests or come back later!`);
} 

else { 
  if (matchCounter == 1) { // one match found
    console.log(`${userProfile.first_name}, we found ${matchCounter} match in your ${userProfile.location} location for you:\r\n`);
  for (let entry of matchesFound) {
    console.log(`${entry.first_name} ${entry.last_name} (${entry.age})\r\n`);
    }
  } 
  
  else { // more than 1 match found  
  console.log(`${userProfile.first_name}, we found ${matchCounter} matches in your ${userProfile.location} location for you:\r\n`);
  for (let entry of matchesFound) {
    console.log(`${entry.first_name} ${entry.last_name} (${entry.age})\r\n`);
    }
  }
}
