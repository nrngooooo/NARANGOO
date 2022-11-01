import { useEffect,useState } from "react";
import styled from "styled-components";
import { useParams } from "react-router-dom";

import React from 'react'

const Recipe = () => {

  let params = useParams();
  const fetchDetails = async () =>{
    const data = await fetch(`https://api.spoonacular.com/recipes/${params.name.REACT_APP_API_KEY}&query=${name}`)
    const recipes = await data.json();  }
  return (
    <div>Recipe</div>
  )
}

export default Recipe