#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE* pixel = &image[i][j];
            float grey_scalePixel = ((float)(*pixel).rgbtRed + (float)(*pixel).rgbtGreen + (float)(*pixel).rgbtBlue) / 3;
            grey_scalePixel = (grey_scalePixel - (int)grey_scalePixel > 0.5) ? (int)grey_scalePixel + 1 : (int)grey_scalePixel;
            (*pixel).rgbtRed = (*pixel).rgbtGreen = (*pixel).rgbtBlue = grey_scalePixel;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average_red = 0, average_green = 0, average_blue = 0, division_count = 0;

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int i_neighbor = i + k;
                    int j_neighbor = j + l;

                    if (i_neighbor >= 0 && i_neighbor < height && j_neighbor >= 0 && j_neighbor < width)
                    {
                        average_red += copy[i_neighbor][j_neighbor].rgbtRed;
                        average_green += copy[i_neighbor][j_neighbor].rgbtGreen;
                        average_blue += copy[i_neighbor][j_neighbor].rgbtBlue;
                        division_count++;
                    }
                }
            }

            image[i][j].rgbtRed = round(average_red / division_count);
            image[i][j].rgbtGreen = round(average_green / division_count);
            image[i][j].rgbtBlue = round(average_blue / division_count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx[3][3] = { {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1} };
    int Gy[3][3] = { {-1, -2, -1}, {0, 0, 0}, {1, 2, 1} };

    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double weighted_redX = 0, weighted_greenX = 0, weighted_blueX = 0;
            double weighted_redY = 0, weighted_greenY = 0, weighted_blueY = 0;

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int i_neighbor = i + k;
                    int j_neighbor = j + l;

                    if (i_neighbor < 0 || i_neighbor > height - 1 || j_neighbor < 0 || j_neighbor > width - 1)
                    {
                        continue;
                    }

                    weighted_redX += copy[i_neighbor][j_neighbor].rgbtRed * Gx[k + 1][l + 1];
                    weighted_greenX += copy[i_neighbor][j_neighbor].rgbtGreen * Gx[k + 1][l + 1];
                    weighted_blueX += copy[i_neighbor][j_neighbor].rgbtBlue * Gx[k + 1][l + 1];

                    weighted_redY += copy[i_neighbor][j_neighbor].rgbtRed * Gy[k + 1][l + 1];
                    weighted_greenY += copy[i_neighbor][j_neighbor].rgbtGreen * Gy[k + 1][l + 1];
                    weighted_blueY += copy[i_neighbor][j_neighbor].rgbtBlue * Gy[k + 1][l + 1];
                }
            }

            double squared_red = sqrt(((weighted_redX * weighted_redX) + (weighted_redY * weighted_redY)));
            double squared_green = sqrt(((weighted_greenX * weighted_greenX) + (weighted_greenY * weighted_greenY)));
            double squared_blue = sqrt(((weighted_blueX * weighted_blueX) + (weighted_blueY * weighted_blueY)));

            squared_red = (squared_red < 0) ? 0 : (squared_red > 255 ? 255 : squared_red);
            squared_green = (squared_green < 0) ? 0 : (squared_green > 255 ? 255 : squared_green);
            squared_blue = (squared_blue < 0) ? 0 : (squared_blue > 255 ? 255 : squared_blue);

            image[i][j].rgbtRed = (int)round(squared_red);
            image[i][j].rgbtGreen = (int)round(squared_green);
            image[i][j].rgbtBlue = (int)round(squared_blue);
        }
    }
    return;
}
