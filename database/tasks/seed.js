const dbConnection = require('../config/mongoConnection');
const data = require('../data/');
const bands = data.bands;
const albums = data.albums;

async function main() {
  const db = await dbConnection.dbConnection();
  await db.dropDatabase();
  console.log("CREATE - BANDS");
    const pinkFloyd = await bands.create("Pink Floyd", ["Progressive Rock", "Psychedelic rock", "Classic Rock"],
    "http://www.pinkfloyd.com", "EMI", ["Roger Waters", "David Gilmour", "Nick Mason", "Richard Wright", "Sid Barrett" ], 1965);
    console.log(pinkFloyd);

    const imagineDragons = await bands.create("Imagine Dragons", ["Alternative Rock", "Pop"],  "http://www.imaginedragonsmusic.com", "Universal Music Group", 
    ["Dan Reynolds", "Daniel Wayne Sermon", "Daniel Platzman", "Ben McKee"], 2009);
    console.log(imagineDragons);

    const BTR= await bands.create("Big Time Rush", ["Pop"], "http://www.bigtimerushofficial.com", "Nickelodeon Records", 
    ["Kendall Schmidt", "Logan Henderson", "Carlos Vega", "James Maslow"], 2009);
    console.log(BTR);

    //got7 website too short so i used BTS
    const GOT7= await bands.create("GOT7", ["K-Pop", "Pop"], "http://www.ibighit.com", "JYPE Entertainment",  
    ["Jaebum", "Yugyeom", "Mark", "Jackson", "Youngjae", "BamBam", "Jinyoung"], 2009);
    console.log(GOT7);

    const theBeatles = await bands.create("The Beatles", ["Rock", "Pop", "Psychedelia"],
    "http://www.thebeatles.com", "Parlophone", ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"], 1960);
    console.log(theBeatles)

// //----------------------------------------------------------------------------------------------------------------------------------------------
  console.log("CREATE - ALBUMS")
    console.log(await albums.create(pinkFloyd._id, "The Dark Side of the Moon", 
    "03/1/2022", 
    ["Shine On You Crazy Diamond, Pts. 1-5", 
    "Welcome to the Machine","Have a Cigar (Ft. Roy Harper)", 
    "Wish You Were Here","Shine On You Crazy Diamond, Pts. 6-9"], 
    4.1));

    const smokeMirrors = await albums.create(imagineDragons._id, "Smoke + Mirrors", 
    "02/17/2015", 
    ["Shots", "Smoke And Mirrors", "Gold", "I'm So Sorry"], 
    2.2);
    console.log(smokeMirrors);

    const mercuryActOne = await albums.create(imagineDragons._id, "Mercury Act 1", 
    "09/03/2021", 
    ["My Life", "Wrecked", "Lonely", "Follow You"], 
    4.5);
    console.log(mercuryActOne);

    const nightvisions = await albums.create(imagineDragons._id, "Night Visions", 
    "02/17/2015", 
    ["Radioactive", "TipToe", "Demons", "On top of the world"], 
    3.6);
    console.log(nightvisions);

    console.log(await albums.create(BTR._id, "BTR", 
    "10/11/2010", 
    ["Til I Forget About You", "Boyfriend", "Count of You", "Halfway There"], 
    2.7));
    
    console.log(await albums.create(GOT7._id, "Present: You", 
    "09/17/2018", 
    ["Lullaby", "Sunrise", "Party", "Fine", "No One Else"], 
    2.8));
    console.log(await albums.create(GOT7._id, "7 for 7", 
    "09/17/2018", 
    ["Teenager", "Remember You", "To Me", "Moon U"], 
    4.4));

    console.log(await albums.create(theBeatles._id, "Abbey Road", 
    "09/26/1969", 
    ["Come Together", "Octopus's Garden", "Oh! Darling"], 
    2.8));

  // getALL
  try{
    console.log("GETALL = Bands");
    const allBands = await bands.getAll();
    console.log(allBands);
  } catch(e) {
    console.log(e);
  }

  try{
  console.log("GETALL - ALBUMS");
  const allAlbums = await albums.getAll(imagineDragons._id.toString());
  console.log(allAlbums);
  } catch(e){
    console.log(e);
  }
    try {
    console.log("GET - BANDS")
    const getImagineDragons = await bands.get(imagineDragons._id.toString());
    console.log(getImagineDragons);
  } catch(e){
    console.log(e);
  }
    // update
    try{
    console.log("UPDATE = Bands");
    const updateImagineDragsons = await bands.update(imagineDragons._id, "Dragons Imagine",
    ["Alternative Rock"],  "http://www.imaginedragonsmusic.com", "Universal Music Group", 
    ["Dan Reynolds", "Daniel Wayne Sermon", "Daniel Platzman", "Ben McKee"], 2009 ); 
    console.log(updateImagineDragsons);
    } catch(e){
      console.log(e)
    }
  try{
  console.log("REMOVE - BANDS");
  const removeImagine = await bands.remove(imagineDragons._id.toString());
   console.log(removeImagine);
  } catch(e) {
    console.log(e);
  }
  // get id
  try{
  console.log("GET = albums");
  const getImagineDragons = await albums.get(nightvisions._id.toString());
  console.log(getImagineDragons);
  } catch(e){
    console.log(e);
  }
 
  try{
  console.log("REMOVE - ALBUMS");
  const removeAlbums = await albums.remove(nightvisions._id.toString());
  console.log(removeAlbums);
  } catch(e){
    console.log(e)
  }
 



  console.log('Done seeding database');

  await dbConnection.closeConnection();
}

main();