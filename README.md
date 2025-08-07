# Electron React Todo App

A beautiful, modern todo application built with Electron and React featuring a glassmorphism design and smooth animations.

## Features

- ✨ Modern glassmorphism UI design
- 📱 Responsive layout that works on all screen sizes
- 🎯 Add, edit, delete, and complete todos
- 🔍 Filter todos by status (All, Active, Completed)
- 💾 Persistent storage using localStorage
- ⌨️ Keyboard shortcuts (Enter to add, Escape to cancel edit)
- 🖥️ Native desktop application with Electron
- 🎨 Beautiful gradient backgrounds and smooth transitions

## Screenshots

The app features a clean, modern interface with:
- Gradient background and glassmorphism effects
- Smooth hover animations and transitions
- Intuitive icons for all actions
- Mobile-responsive design

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

### Development

To run the app in development mode:

```bash
# Start React development server and Electron app
npm run dev
```

This will:
- Start the React development server on http://localhost:3000
- Launch the Electron app which loads the React app
- Enable hot reloading for both React and Electron

### Building for Production

1. Build the React app:
```bash
npm run build
```

2. Build the Electron app:
```bash
npm run electron-build
```

The built application will be available in the `dist` folder.

### Running Individual Components

- React only: `npm start`
- Electron only (after building React): `npm run electron`

## Project Structure

```
electron-react-todo/
├── public/
│   ├── index.html          # HTML template
│   └── main.js            # Electron main process
├── src/
│   ├── App.js             # Main React component
│   ├── App.css            # App styles
│   ├── index.js           # React entry point
│   └── index.css          # Global styles
├── package.json           # Dependencies and scripts
└── README.md             # This file
```

## Technologies Used

- **Electron**: Cross-platform desktop app framework
- **React**: UI library for building user interfaces
- **Lucide React**: Beautiful icon library
- **CSS3**: Modern styling with gradients and glassmorphism
- **localStorage**: For persistent data storage

## Features Overview

### Todo Management
- Add new todos with the plus button or Enter key
- Mark todos as complete/incomplete with the checkbox
- Edit todos inline with the edit button
- Delete todos with the trash button
- Clear all completed todos at once

### Filtering
- **All**: Show all todos
- **Active**: Show only incomplete todos
- **Completed**: Show only completed todos

### Keyboard Shortcuts
- `Enter`: Add new todo or save edit
- `Escape`: Cancel edit
- `Ctrl/Cmd + N`: Focus on new todo input (from menu)

### Data Persistence
All todos are automatically saved to localStorage and restored when the app is reopened.

## Customization

### Changing Colors
Edit the CSS variables in `src/App.css` and `src/index.css` to customize the color scheme.

### Adding Features
The app is built with a modular structure, making it easy to add new features like:
- Todo categories
- Due dates
- Priority levels
- Search functionality
- Export/import

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - feel free to use this project for learning or as a starting point for your own applications.

## Troubleshooting

### Common Issues

1. **App won't start**: Make sure all dependencies are installed with `npm install`
2. **Build fails**: Ensure you have Node.js 14+ installed
3. **Electron security warnings**: These are normal in development mode

### Performance Tips

- The app uses React's built-in optimizations
- localStorage is used for persistence (efficient for small datasets)
- CSS transitions are GPU-accelerated for smooth animations

## Support

If you encounter any issues or have questions, please check the existing issues or create a new one in the repository.