import React, { useState } from "react";
import { Link } from "react-router-dom";
import Button from "../components/button/Button";
import Frame from "../components/Frame/Frame";
import Input from "../components/input/Input";
import Select from "../components/select/Select";

/**
 * Choosing a mode and opening block where players can input their names
 * 
 * @param {event} e Get value from Select form
 * @param {string} setMode Save selected mode in "mode" variable
 */

const selectValue = (e, setMode) => {
  const value = e.target.value;
  console.log(value); 
  if (value === "1") {
    document.getElementsByClassName("multi")[0].style.display = "none";
    document.getElementsByClassName("single")[0].style.display = "block";
    setMode("A Single Game");
  } else {
    document.getElementsByClassName("single")[0].style.display = "none";
    document.getElementsByClassName("multi")[0].style.display = "block";
    setMode("Multiplayer Game");
  }
  document.getElementById("playBtn").disabled=false
};

/**
 * Rendering the Second Page: Modes, Name of Players
 * 
 * @returns React Component
 */

const Selections = () => {
  const [mode, setMode] = useState("?");
  const [player1, setPlayer1] = useState("player1");
  const [player2, setPlayer2] = useState("player2");

  return (
    <center>
      <Frame style={{ width: "50%", height: "450px" }}>
        <center>
          <h1>Hello!</h1>
        </center>
        Please choose mode of the game:
        <br />
        <Select
          onChange={(event) => selectValue(event, setMode)}
          defaultValue={"DEFAULT"}
        >
          <option disabled value="DEFAULT">
            Modes
          </option>
          <option value="1">A Single Game</option>
          <option value="2">Multiplayer Game</option>
        </Select>
        <div className="modes">
          <div className="single">
            Player's Name:
            <Input onChange={(event) => setPlayer1(event.target.value)} placeholder="player1"/>
          </div>
          <div className="multi">
            The First Player's Name
            <Input onChange={(event) => setPlayer1(event.target.value)} placeholder="player1"/>
            The Second Player's Name
            <Input onChange={(event) => setPlayer2(event.target.value)} placeholder="player2"/>
          </div>
          <div className="info">
            Inputed Info : <br />
            Mode <b>{mode}</b>
            <br />
            1st Player <b>{player1}</b>
            <br />
            2nd Player <b>{player2}</b>
            <br />
            <Link to="../game" state={{ from: { player1, player2, mode } }}>
              <Button id="playBtn" className="right" disabled>Play</Button>
            </Link>
          </div>
        </div>
      </Frame>
    </center>
  );
};

export default Selections;
