# Mapa de Gross Domestic Product (GDP)

# instalar e carregar os pacotes necessários

install.packages("foreign")
install.packages ("ggplot2")
install.packages ("ggmap")
install.packages ("reshape2")
install.packages ("maps")
install.packages ("Cairo")

library(foreign)
library(ggplot2)
library(ggmap)
library(reshape2)
library(maps)
library(Cairo)

# importar os dados e função attach

library(readxl)
economia <- read_excel("economia.xls")
View(economia)

attach(economia)

# separar as variáveis “country” e “gdp__billions_” (criar um subset)

econ <- subset(economia, select=c(country, gdp__billions_))

# carregar o mapa mundi do R chamado world

world = map_data("world")

# Utilizar a função merge para unir os objetos econ e world

world1 <- merge (world, econ, by.x="region", by.y="country", all.x=T, all.y=F)

# Reordenar o novo objeto criado

world1 <- world1[order(world1$order),]

# Gerar mapa e legenda

m0 <- ggplot(data=world1)
m1 <- m0 + geom_polygon(aes(x=long, y=lat, group=group, fill= gdp__billions_)) + coord_equal()
m2 <- m1 + geom_path(aes(x=long, y=lat, group=group), color='grey', linewidth=.1) #Using `size` aesthetic for lines was deprecated in ggplot2 3.4.0. Please use `linewidth` instead.#
m3 <- m2 + scale_fill_gradient(low = "#88ddff", high = "darkblue")

m3

# Salvar o mapa em PNG

ggsave("GDP_map.png", plot = m3, width = 7, height = 3.5, units = "in", dpi = 1500)