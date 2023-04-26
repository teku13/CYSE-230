import QtQuick 6
import QtQuick.Window 2.15
import QtQuick.Controls 6
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window 
    width: 760
    height: 500
    visible: true
    title: qsTr("App Home")

    // SET MATERIAL STYLE
    Material.theme: Material.Light
    Material.accent: Material.LightOrange

    // CUSTOM PROPERTIES
    property string textUsername: "User"
    property string textPassword: "Pass"

    // Labels
    // SHOWS USER
    Text{
        id: textUser
        text: textUsername
        anchors.verticalCenter: parent.verticalCenter
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: "#000000"
        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: 10
    }

    // SHOWS PASSWORD
    Text{
        id: textPass
        text: textPassword
        anchors.verticalCenter: parent.verticalCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.margins: 10
        anchors.top: textUser.bottom
        anchors.topMargin: 20
        color: "#000000"
        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: 10
    }
}