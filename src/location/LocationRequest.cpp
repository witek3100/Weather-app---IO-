#include "LocationRequest.h"
#include <iostream>
#include <wlanapi.h>
#include <windows.h>


using namespace std;

int LocationRequest::getWifiAccessPoints() {

    HANDLE hClient = NULL;
    DWORD dwMaxClient = 2;
    DWORD dwCurVersion = 0;
    DWORD dwResult = 0;
    DWORD dwBResult = 0;
    DWORD dwRetVal = 0;
    wifiAccessPoint accessPoint{ "00:00:00:00:00:00", 0 };

    PWLAN_INTERFACE_INFO_LIST pIfList = NULL;
    PWLAN_INTERFACE_INFO  pIfInfo = NULL;
    PWLAN_BSS_LIST pBssList = NULL;
    PWLAN_BSS_ENTRY pBssEntry = NULL;

    dwResult = WlanOpenHandle(dwMaxClient, NULL, &dwCurVersion, &hClient);
    if (dwResult != ERROR_SUCCESS){
         std::cerr << "ERROR";
         return 1;
    }

    dwResult = WlanEnumInterfaces(hClient, NULL, &pIfList);
    if (dwResult != ERROR_SUCCESS){
        cerr << "ERROR2";
        return 1;
    } else {
        for (int i=0; i<(int)pIfList->dwNumberOfItems; i++){
            pIfInfo = (WLAN_INTERFACE_INFO *)&pIfList->InterfaceInfo[i];
            dwBResult = WlanGetNetworkBssList(hClient, &pIfInfo->InterfaceGuid, NULL, dot11_BSS_type_any, 0, 0, &pBssList);
            if (dwBResult != ERROR_SUCCESS){
                cerr << "ERROR3";
                dwRetVal = 1;
            } else {
                cout << endl << "Found " << pBssList->dwNumberOfItems << " access points" << endl;
                for (int j=0; j<pBssList->dwNumberOfItems; j++){
                    pBssEntry = (WLAN_BSS_ENTRY *)& pBssList->wlanBssEntries[j];
                    sprintf(accessPoint.macAdress,"%02X:%02X:%02X:%02X:%02X:%02X",
                            pBssEntry->dot11Bssid[0],
                            pBssEntry->dot11Bssid[1],
                            pBssEntry->dot11Bssid[2],
                            pBssEntry->dot11Bssid[3],
                            pBssEntry->dot11Bssid[4],
                            pBssEntry->dot11Bssid[5]);
                    accessPoint.signalQuality = pBssEntry->lRssi;
                    wifiAccessPointsList.push_back(accessPoint);
                }
            }
        }
    }
}


char *LocationRequest::buildRequestJSON() {}

void LocationRequest::getLocation() {}

void LocationRequest::printLocation() {}
