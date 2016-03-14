package main

import "math"
import "fmt"

func main(){
  fmt.Println(sin(0));
  fmt.Println(sin(math.Pi));
  fmt.Println(sin(1));
}

func sin(x float64) float64{
  return sin_wrapped(x, 107, true, 0);
}

func sin_wrapped(x float64, depth float64, sign bool, sum float64) float64{
  if depth == 1 {
    return x + sum
  } else if sign == true {
    return sin_wrapped(x, depth-2, false, sum-(math.Pow(x, depth)/factorial(depth)));
  } else {
    return sin_wrapped(x, depth-2, true, sum+(math.Pow(x, depth)/factorial(depth)));
  }
}

func factorial(x float64) float64{
	if x == 0 {
		return 1
	}
	return x * factorial(x-1)
}
