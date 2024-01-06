import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import Frame from "../components/Frame/Frame";
import Button from "../components/button/Button";
import Games from "../components/game/Game";

/**
 * The Third Page: rendering the game
 * 
 * @returns React Component
 */

const Game = () => {
  let [count1, setCount1] = useState(0);
  let [count2, setCount2] = useState(0);
  const [sign, setSign] = useState("X");
  let [boardArray, setBoardArray] = useState(new Array(9).fill(false, 0, 9));
  const [win, setWin] = useState("");

  const location = useLocation();
  const { from } = location.state;

  console.log("call");

  /**
   * Cleaning board and set default Sign ('X')
   */

  const newGame = () => {
    setBoardArray(new Array(9).fill(false, 0, 9));
    document.getElementById("board").style.pointerEvents = "auto";
    setSign("X");
    setWin("")
  };

  return (
    <center>
      <Frame style={{ width: "50%"}}>
        <center>
          <h2 style={{ marginTop: "0", height: '10%' }}>Count</h2>
        </center>
        <div className="players">
          <h3>
            {from["player1"]}
            <br />
            {count1}
          </h3>
          <h3>
            {from["player2"]}
            <br />
            {count2}
          </h3>
        </div>
        <Games
          boardArray={boardArray}
          sign={sign}
          setSign={setSign}
          count1={count1}
          setCount1={setCount1}
          count2={count2}
          setCount2={setCount2}
          player1={from["player1"]}
          player2={from["player2"]}
          modeIs={from["mode"]}
          setWin={setWin}
        />
        <center>
          <h2>
            {win}
          </h2>
          <Button onClick={newGame}>
          Continue
        </Button>
        </center>
      </Frame>
    </center>
  );
};

export default Game;
