import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/button/Button";
import Frame from "../components/Frame/Frame";

/**
 * The First Page: Rules of the Game
 * 
 * @returns React Component
 */

const Introduce = () => {
  return (
    <center>
        <Frame style={{ width: "30%", paddingBottom: "50px"}}>
          <b className="title">Inroduction</b>
          <p>
            Tic-tac-toe is a paper-and-pencil game for two players who take turns
            marking the spaces in a three-by-three grid with X or O. The player who
            succeeds in placing three of their marks in a horizontal, vertical, or
            diagonal row is the winner. It is a solved game, with a forced draw
            assuming best play from both players.
          </p>
          <Link to="selections">
            <Button className="right">Next</Button>
          </Link>
        </Frame>
    </center>
  );
};

export default Introduce;
