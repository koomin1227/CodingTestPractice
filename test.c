//#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
//#include <windows.h>
#include <math.h>
typedef unsigned long DWORD;
typedef unsigned short WORD;
typedef long LONG;
typedef struct tagBITMAPFILEHEADER {
  WORD  bfType;
  DWORD bfSize;
  WORD  bfReserved1;
  WORD  bfReserved2;
  DWORD bfOffBits;
} BITMAPFILEHEADER, *LPBITMAPFILEHEADER, *PBITMAPFILEHEADER;

typedef struct _tagBITMAPINFOHEADER {
  DWORD biSize;
  LONG  biWidth;
  LONG  biHeight;
  WORD  biPlanes;
  WORD  biBitCount;
  DWORD biCompression;
  DWORD biSizeImage;
  LONG  biXPelsPerMeter;
  LONG  biYPelsPerMeter;
  DWORD biClrUsed;
  DWORD biClrImportant;
} BITMAPINFOHEADER;

int main() {

	BITMAPFILEHEADER bmpFile, bmpFile1;
	BITMAPINFOHEADER bmpInfo, bmpInfo1;
	FILE *inputFile1 = NULL, *inputFile2 = NULL;
	inputFile1 = fopen("AICenterY.bmp", "rb");
	inputFile2 = fopen("AICenterY_CombinedNoise.bmp", "rb");
	fread(&bmpFile, sizeof(BITMAPFILEHEADER), 1, inputFile1);
	fread(&bmpInfo, sizeof(BITMAPINFOHEADER), 1, inputFile1);
	fread(&bmpFile1, sizeof(BITMAPFILEHEADER), 1, inputFile2);
	fread(&bmpInfo1, sizeof(BITMAPINFOHEADER), 1, inputFile2);

	int width = bmpInfo.biWidth;
	int height = bmpInfo.biHeight;
	int size = bmpInfo.biSizeImage;
	int bitCnt = bmpInfo.biBitCount;
	int stride = (((bitCnt / 8) * width) + 3) / 4 * 4;
	double *Y1, Cb, Cr, R, G, B, *Y2;
	double diff_Y;

	unsigned char I;
	printf("W: %d(%d)\nH: %d\nS: %d\nD: %d\n\n", width, stride, height, size, bitCnt);

	unsigned char *inputImg = NULL, *outputImg = NULL, *inputImg1 = NULL;
	inputImg = (unsigned char *)calloc(size, sizeof(unsigned char));
	inputImg1 = (unsigned char *)calloc(size, sizeof(unsigned char));
	outputImg = (unsigned char *)calloc(size, sizeof(unsigned char));
	fread(inputImg, sizeof(unsigned char), size, inputFile1);
	fread(inputImg1, sizeof(unsigned char), size, inputFile2);

	//Original Copy
	double mse = 0, psnr;
	Y1 = (double *)calloc(sizeof(double), (width * height));
	Y2 = (double *)calloc(sizeof(double), (width * height));
	for (int j = 0; j < height; j++)
	{
		for (int i = 0; i < width; i++)
		{
			Y1[j * width + i] = inputImg[j * stride + 3 * i + 0];
			Y2[j * width + i] = inputImg1[j * stride + 3 * i + 0];
			if (j == 0 || j == width - 1 || i == 0 || i == height - 1)
			{
				outputImg[j * stride + 3 * i + 0] = inputImg1[j * stride + 3 * i + 0];
				outputImg[j * stride + 3 * i + 1] = inputImg1[j * stride + 3 * i + 0];
				outputImg[j * stride + 3 * i + 2] = inputImg1[j * stride + 3 * i + 0];
			}
			//Y2 = 0.299  * inputImg1[j * stride + 3 * i + 2] + 0.587 * inputImg1[j * stride + 3 * i + 1] + 0.114 * inputImg1[j * stride + 3 * i + 0];
			//Y2 = (unsigned char)(Y2 > 255 ? 255 : (Y2 < 0 ? 0 : Y2));
			//mse += (double)((Y2 - Y1)*(Y2 - Y1));









			//Y = 0.299  * inputImg[j * stride + 3 * i + 2] + 0.587 * inputImg[j * stride + 3 * i + 1] + 0.114 * inputImg[j * stride + 3 * i + 0];
			//Cb = -0.169 * inputImg[j * stride + 3 * i + 2] - 0.331 * inputImg[j * stride + 3 * i + 1] + 0.500 * inputImg[j * stride + 3 * i + 0];
			//Cr = 0.500 * inputImg[j * stride + 3 * i + 2] - 0.419 * inputImg[j * stride + 3 * i + 1] - 0.0813 * inputImg[j * stride + 3 * i + 0];
			//I = (unsigned char)((inputImg[j * stride + 3 * i + 2] + inputImg[j * stride + 3 * i + 1] + inputImg[j * stride + 3 * i + 0]) / 3);
			////outputImg[j * stride + 3 * i + 0] = (unsigned char)(Y > 255 ? 255 : (Y < 0 ? 0 : Y));
			////outputImg[j * stride + 3 * i + 1] = (unsigned char)(Y > 255 ? 255 : (Y < 0 ? 0 : Y));
			////outputImg[j * stride + 3 * i + 2] = (unsigned char)(Y > 255 ? 255 : (Y < 0 ? 0 : Y));
			////outputImg[j * stride + 3 * i + 0] = I;
			////outputImg[j * stride + 3 * i + 1] = I;
			////outputImg[j * stride + 3 * i + 2] = I;
			//diff_Y= (Y - I)*(Y - I);
			//outputImg[j * stride + 3 * i + 0] = (unsigned char)(diff_Y > 255 ? 255 : (diff_Y < 0 ? 0 : diff_Y));
			//outputImg[j * stride + 3 * i + 1] = (unsigned char)(diff_Y > 255 ? 255 : (diff_Y < 0 ? 0 : diff_Y));
			//outputImg[j * stride + 3 * i + 2] = (unsigned char)(diff_Y > 255 ? 255 : (diff_Y < 0 ? 0 : diff_Y));
			///*Y = Y + 20;
			//R = (Y + 100) + 1.402 * Cr;
			//G = (Y + 100) - 0.714 * Cr - 0.344 *Cb;
			//B = (Y + 100) + 1.772 * Cb;
			//outputImg[j * stride + 3 * i + 2] = (unsigned char)(R > 255 ? 255 : (R < 0 ? 0 : R));
			//outputImg[j * stride + 3 * i + 1] = (unsigned char)(G > 255 ? 255 : (G < 0 ? 0 : G));
			//outputImg[j * stride + 3 * i + 0] = (unsigned char)(B > 255 ? 255 : (B < 0 ? 0 : B));*/
			////printf("%lf", Y);
		}
	}
	double filter[3][3] = { {1.0 / 9,1.0 / 9,1.0 / 9},{1.0 / 9,1.0 / 9,1.0 / 9},{1.0 / 9,1.0 / 9,1.0 / 9} };
	double res;
	for (int j = 1; j < height-1; j++)
	{
		for (int i = 1; i < width-1; i++)
		{
			res = 0;
			for (int k = j - 1; k < j + 2; k++)
				for (int l = i - 1; l < i + 2; l++)
					res = res + (filter[k - (j - 1)][l - (i - 1)] * Y2[k*width + l]);
			outputImg[j * stride + 3 * i + 0] = (unsigned char)res;
			outputImg[j * stride + 3 * i + 1] = (unsigned char)res;
			outputImg[j * stride + 3 * i + 2] = (unsigned char)res;
		}
	}

	for (int j = 0; j < height; j++)
	{
		for (int i = 0; i < width; i++)
		{
			mse += (double)((Y2[j*width + i] - Y1[j*width + i])*(Y2[j*width + i] - Y1[j*width + i]));
		}
	}
	mse /= (width *height);
	psnr = mse != 0.0 ? 10.0* log10(255 * 255 / mse) : 99.99;
	printf("MSE = %.2lf\nPSNR = %.2lf db\n", mse, psnr);
	FILE *outputFile = fopen("Output_border.bmp", "wb");
	fwrite(&bmpFile, sizeof(BITMAPFILEHEADER), 1, outputFile);
	fwrite(&bmpInfo, sizeof(BITMAPINFOHEADER), 1, outputFile);
	fwrite(outputImg, sizeof(unsigned char), size, outputFile);

	free(outputImg);
	free(inputImg);
	fclose(inputFile1);
	fclose(inputFile2);
	fclose(outputFile);
	return 0;
}