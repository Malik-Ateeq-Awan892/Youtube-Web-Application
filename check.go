package main

import "fmt"

var channels []Channel //slice to store channels

type Channel struct { //channel struct
	channel_title string
	channel_desc  string
	channel_url   string
}

func Display(c Channel) { //display function
	fmt.Println("Channel Title:	:", c.channel_title, "\nChannel Description:	:", c.channel_desc, "\nChannel URL:	:", c.channel_url)
}

func Add_Channel() Channel { //function to add new channel to the slice
	var c1 Channel
	fmt.Println("Enter the title of channel")
	fmt.Scanln(&c1.channel_title)
	fmt.Println("Enter the description of the channel")
	fmt.Scanln(&c1.channel_desc)
	fmt.Println("Enter the url of the channel")
	fmt.Scanln(&c1.channel_url)
	channels = append(channels, Channel{c1.channel_title, c1.channel_desc, c1.channel_url}) //adding channel to slice
	return c1

}
func Delete_Channel() { // method to delete channel by name from the slice
	var name string // var to get channel name
	fmt.Println("Enter the name of the channel to delete")
	fmt.Scanln(&name)
	for i := 0; i < len(channels); i++ { //loop to iterate in the slice
		if channels[i].channel_title == name {
			channels = append(channels[:i], channels[i+1:]...) //removing the index where nsme is found
			fmt.Println("Channel", name, "deleted successfully")
			return
		}
	}
	fmt.Println("Channel", name, "not found") //print if channel not found
}

func Display_All() {
	for i := 0; i < len(channels); i++ { //loop to iterate in the slice
		fmt.Println("\nChannel : ", i+1)
		Display(channels[i]) //calling display function for each index or object
	}
}

func main() {
	var c1 Channel
	c1.channel_title = "airbnb"
	c1.channel_desc = "booking"
	c1.channel_url = "https://www.airbnb.com/"
	fmt.Println(c1)
	Add_Channel()
	Display(channels[0])
	Add_Channel()
	Add_Channel()
	Display_All()
	Delete_Channel()
	Display_All()
}
