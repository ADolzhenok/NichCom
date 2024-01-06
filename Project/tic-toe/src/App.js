import "./App.css";
import React from "react";
import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Selections from "./pages/Selections";
import Introduce from "./pages/Introduce";
import Game from "./pages/Game";

/*
* Main App. Switching between Introduce, Selections and Game pages
*/ 

function App() {
  return (
    <div id="main">
      <Header />
      <BrowserRouter>
        <Routes>
          <Route index element={<Introduce />} />
          <Route path="selections" element={<Selections />}></Route>
          <Route path="game" element={<Game />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
