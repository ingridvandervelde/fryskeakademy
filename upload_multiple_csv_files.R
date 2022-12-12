library(shiny)
library(readr)
library(ggplot2)

# create some data to upload
write_csv(mtcars, "mtcars.csv")
write_csv(mpg   , "mpg.csv")
write_csv(iris  , "iris.csv")

options(shiny.maxRequestSize = 30 * 1024^2)

ui <- fluidPage(
  fileInput("upload", NULL, buttonLabel = "Upload...", multiple = TRUE),
  htmlOutput("fileNames"),
  
)

server <- function(input, output, session) 
{
  global <- reactiveValues(allebestanden = list())

  output$fileNames <- renderText(
  { 
    # show file names
    
    req(input$upload)
    
    fN <- "File names:<br><br>"
    
    for (i in 1:length(input$upload$name))
    {
      fN <- paste0(fN, input$upload$name[i], "<br>")
    }
    
    return(HTML(fN))
  })
  
    
  observeEvent(input$upload,
  {
    # read files
    
    for (i in 1:length(input$upload$name))
    {
      global$allebestanden[[i]] <- read_csv(input$upload$datapath[i])
    }
  })

  observeEvent(global$allebestanden,
  {
    if (length(global$allebestanden) > 0)
    {
      # view files
      
      for (i in 1:length(global$allebestanden))
      {
        fName <- paste("file", as.character(i), sep = "")
        assign(fName, global$allebestanden[[i]])
        do.call(View, list(as.name(fName)))
      }
    }
  })
}

shinyApp(ui, server)